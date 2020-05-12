import sys
import time
from collections import Counter, defaultdict

if len(sys.argv) != 2:
    print('usage: python3 create_degree_list.py <subject_adjacency.txt')
    exit()

with open('node_ids.txt') as fp:
    nodes = fp.readlines()

node_set = set()
for node in nodes:
    node = node.strip()
    name, node = node.split('\t')
    node_set.add(int(node))

filename = sys.argv[1]
data = [line.rstrip('\n') for line in open(filename)]


data_dict = defaultdict(set)

for adj in data:
    key, members = adj.split('\t', 1)
    adj_set = {int(m) for m in members.split('|')}
    if len(adj_set) > 1:
        member_tuple = tuple(sorted(adj_set))
        data_dict[member_tuple[0]].add(member_tuple[1:])


DEGREE_DATA = Counter()
DEGREE_DATA_UPDATE = DEGREE_DATA.update  # Performance hack?
TOTAL_NODES = len(node_set)
START_TIME = time.time()

for working in sorted(node_set):

    if working in data_dict:
        adj_set = set()
        adj_set_update = adj_set.update  # Performance hack?
        working_remove = data_dict[working].remove  # Performance hack?
        for member_tuple in list(data_dict[working]):
            adj_set_update(member_tuple)

            # At some point member_tuple will only have 1 item, we stop there.
            if len(member_tuple) > 1:
                # Take first item in member, add to dict if need
                data_dict[member_tuple[0]].add(member_tuple[1:])

            working_remove(member_tuple)  # Performance hack?

        # At this point we should have nothing left for working.
        del data_dict[working]

        # Update full degree data
        adj_set_len = len(adj_set)
        DEGREE_DATA[working] += adj_set_len
        # This increments each item in the adj_set because Counter!
        DEGREE_DATA_UPDATE(adj_set)
    else:
        DEGREE_DATA[working] += 0

    if working % 100 == 0:
        elapsed_time = time.time() - START_TIME

        print('{:,} nodes worked of {:,}: Last 100 in {:.2f} sec'.format(working, TOTAL_NODES, elapsed_time), file=sys.stderr)

        START_TIME = time.time()

for k in sorted(DEGREE_DATA):
    node = k
    degree = DEGREE_DATA[k]
    print('{}\t{}'.format(node, degree))
