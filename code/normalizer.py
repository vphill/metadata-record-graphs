import fileinput
import unicodedata
import string
import argparse

import naco


def remove_punct(value):
    """Converts string by removing punctuation characters."""
    value = value.strip()
    value = value.translate(str.maketrans('', '', string.punctuation))
    return value


def normalize_whitespace(value):
    """Removes repeated whitespace from string"""
    value = " ".join(value.split())
    return value


def lower_case(value):
    """Converts string by removing whitespace and lower-casing all chars."""
    value = value.strip()
    value = value.lower()
    return value


def strip_accents(value):
    """Removes character marks which do not add to the width of a character.

    One simple example of this would be removing the accents from a spanish
    string and returning (non-extended) ASCII. However, it does not mean only
    ASCII characters will be returned. Marks which do add width will not be
    removed, and the character which the mark is being applied to will be
    returned unchanged.
    """
    return ''.join(c for c in unicodedata.normalize('NFD', value)
                   if unicodedata.category(c) != 'Mn')


def to_ascii(value):
    """Cluster by removing marks (like accents) from all chars and stripping whitespace.

    This has the effect of appearing to convert some unicode strings to ASCII, but that
    is really only the case in certain circumstances where the only non-ASCII characters
    in the string can be normalized to an ASCII character combined with certain marks.
    See strip_accents docstring for more details on the accent removal process.
    """
    value = value.strip()
    value = strip_accents(value)
    return value


def fingerprint(value, punct=' ', keep_digits=True):
    """More thorough clustering method.

    This clustering strips all leading/trailing whitespace as well as
    merging consecutive whitespace, lower-casing all values, removing certain
    character marks, deleting or replacing punctuation with spaces (depending
    on value of punct), keeping or discarding digits (depending on truthiness
    of keep_digits), and then alphabetically sorting the string by words.
    """
    new_value = list(value.lower())
    for i, char in enumerate(new_value):
        if char.isalpha():
            # Keep lower-cased ASCII chars.
            if char in string.ascii_lowercase:
                continue
            # Convert Unicode to ASCII if possible, drop if not.
            else:
                new_value[i] = strip_accents(char)
        # Replace punctuation with value of punct.
        elif not char.isdigit():
            new_value[i] = punct
        # Keep digits if keep_digits is True, otherwise replace them with spaces.
        elif keep_digits:
            continue
        else:
            new_value[i] = ' '

    new_value = ''.join(new_value)
    # Split to strip leading/trailing whitespace and remove consecutive whitespace.
    value_parts = new_value.split()
    # Rejoin in sorted order.
    value = ' '.join(sorted(set(value_parts)))
    return value


def normalize_naco(value):
    """Use NACO normalization rules from UNT Libraries pynaco"""

    value = value.strip()

    return naco.normalizeSimplified(value)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--lowercase', action='store_true',
                        help='Lowercase the values')
    parser.add_argument('-p', '--punctuation', action='store_true',
                        help='Remove punctuation from values')
    parser.add_argument('-w', '--whitespace', action='store_true',
                        help='Remove redundant whitespace from values')
    parser.add_argument('-u', '--unaccent', action='store_true',
                        help='Normalize extended western characters to their ASCII representation')
    parser.add_argument('--naco', action='store_true',
                        help='Apply NACO normalization algorithm to values')

    parser.add_argument('--fingerprint', action='store_true',
                        help='Apply fingerprint algorithm to values')

    parser.add_argument('files', metavar='FILE', nargs='*',
                        help='files to read, if empty, stdin is used')
    args = parser.parse_args()

    # If you would call fileinput.input() without files it would try
    # to process all arguments. We pass '-' as only file when argparse got
    # no files which will cause fileinput to read from stdin
    for line in fileinput.input(files=args.files if args.files else ('-', )):
        line = line.strip()
        value, identifier = line.rsplit('\t', 1)

        if args.naco:
            value = normalize_naco(value)

        if args.fingerprint:
            value = fingerprint(value)
        else:
            if args.lowercase:
                value = lower_case(value)
            if args.punctuation:
                value = remove_punct(value)
            if args.whitespace:
                value = normalize_whitespace(value)
            if args.unaccent:
                value = to_ascii(value)

        if value.strip() == '':
            continue
        print('{}\t{}'.format(value, identifier))
