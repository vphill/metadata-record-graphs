# -*- coding: utf-8 -*-
"""
This will convert the identifiers with their integer
identifiers (intid) that are stored in node_ids.txt

The input is a two column file separated with a tab
character. The first column is the identifier and the
second is the string value for the element.


Output is a two column file separated with a tab
character. This script inverts the output so that the
first column is now the field data value and the second
value is the mapped identifier from node_ids.txt

"""
import fileinput

with open('node_ids.txt') as fp:
    NODE_IDS = fp.readlines()

ID_MAPPING = {}

for line in NODE_IDS:
    line = line.strip()
    name, int_id = line.split('\t')
    ID_MAPPING[name] = int_id

for line in fileinput.input():
    line = line.strip()

    name, value = line.split('\t')
    new_name = ID_MAPPING[name]

    print('{}\t{}'.format(value, new_name))
