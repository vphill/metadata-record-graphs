# -*- coding: utf-8 -*-
"""
This script will add nodes from node_ids.txt that are
unconnected back into the final degree list. These will
have a degree of zero.

Output is a two columen, tab separated list with the
first column the integer identifier (intid) and the second
column the degree of that node.

"""
import fileinput

with open('node_ids.txt') as fp:
    nodes = fp.readlines()

node_set = set()
for node in nodes:
    node = node.strip()
    name, node = node.split('\t')
    node_set.add(node)

connected_nodes = set()
for line in fileinput.input():
    line = line.strip()

    code, degree = line.split('\t')

    connected_nodes.add(code)

    print(line)

unconnected_nodes = node_set - connected_nodes
for node in unconnected_nodes:
    print('{}\t{}'.format(node, 0))
