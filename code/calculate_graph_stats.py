import fileinput
import statistics


def gini(list_of_values):
    sorted_list = sorted(list_of_values)
    height, area = 0, 0
    for value in sorted_list:
        height += value
        area += height - value / 2.
    fair_area = height * len(list_of_values) / 2.
    return (fair_area - area) / fair_area


node_set = set()
total_degrees = 0
degrees = []
node_count = 1
connected_node_set = set()
weight_averages = []
degree_list = []
for line in fileinput.input():

    line = line.strip()

    node, degree = line.split('\t', 1)
    degree = int(degree)
    degrees.append(float(degree))
    total_degrees += degree
    node_set.add(node)

    if degree != 0:
        connected_node_set.add(node)

    degree_list.append(degree)

max_degree = max(degree_list)

if max_degree > 0:
    qlink_list = [x / max_degree for x in degree_list]
    qlink_mean = statistics.mean(qlink_list)
    qlink_std = statistics.stdev(qlink_list)
else:
    qlink_mean = 0.0
    qlink_std = 0.0

unconnected_node_set = node_set - connected_node_set
connected_nodes = len(connected_node_set)
unconnected_nodes = len(unconnected_node_set)

total_nodes = len(list(node_set))

total_edges = int(total_degrees / 2)

possible_edges = (total_nodes * (total_nodes-1)) / 2

density = total_edges / possible_edges

average_degree = (2 * total_edges) / total_nodes

if connected_nodes and total_degrees:
    gini_coefficient = gini(degrees)
else:
    gini_coefficient = 0.0


print('\t'.join([
    str(connected_nodes),
    str(unconnected_nodes),
    str(total_edges),
    str(density),
    str(average_degree),
    str(qlink_mean),
    str(qlink_std)
    ]))
