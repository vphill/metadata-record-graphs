# -*- coding: utf-8 -*-
"""
Convert a list of identifiers to unique integers
that will be used in place of identifiers throughout
the rest of this code workflow.

Output is a two columen, tab separated list with the
first column the original identifier and the second
column the integer assigned to that identifier.

"""
import fileinput


COUNTER = 1
NODES = set()
for line in fileinput.input():
    line = line.strip()
    node_id = COUNTER
    if line not in NODES:
        print('{}\t{}'.format(line, node_id))
        NODES.add(line)
        COUNTER += 1
    else:
        pass
