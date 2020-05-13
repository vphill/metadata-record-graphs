#!/bin/bash
echo "Testing Code"

echo "creating node_ids.txt"
python3 ../code/node_list_to_intids.py nodes.txt > node_ids.txt

echo "Replacing identifiers with intids"
python3 ../code/replace_ids_with_intid.py ark_value.txt > subject_value_int.txt

echo "Normalizing values"
python3 ../code/normalizer.py --naco subject_value_int.txt > subject_normalized_value_int.txt

echo "Sorting value_int"
LC_ALL=C sort -T . -S 20G subject_normalized_value_int.txt -o subject_value_int_sorted.txt

echo "Creating Adjacency"
python3 ../code/create_adjacency_list.py subject_value_int_sorted.txt > subject_value_adjacency.txt

echo "Creating Degree List"
python3 ../code/create_degree_list.py subject_value_adjacency.txt > subject_degree_list.txt

echo "Changing intids to original identifiers"
python3 ../code/replace_intid_with_identifier.py  subject_degree_list.txt > subject_degree_complete.txt

echo "Calculating Graph Stats"
python3 ../code/calculate_graph_stats.py subject_degree_complete.txt

echo "Calculating Degree Stats"
python3 ../code/calculate_degree_stats.py subject_degree_complete.txt

echo "\nCleaning up test files"
rm node_ids.txt
rm subject*.txt
