import fileinput

working_value = ''
identifiers = []

for line in fileinput.input():
    line = line.strip()

    value, m_id = line.split('\t', 1)

    # Set first iteration to the first value
    if working_value == '':
        working_value = value

    # If we've seen this value just append the value
    if working_value == value:
        identifiers.append(m_id)
    else:
        print('{}\t{}'.format(working_value, '|'.join(identifiers)))
        identifiers = [m_id]
        working_value = value

print('{}\t{}'.format(working_value, '|'.join(identifiers)))
