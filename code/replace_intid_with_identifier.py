import fileinput

with open('node_ids.txt') as fp:
    data = fp.readlines()

code_mapping = {}

for line in data:
    line = line.strip()
    name, code = line.split('\t')
    code_mapping[code] = name

for line in fileinput.input():
    line = line.strip()

    code, degree = line.split('\t')

    name = code_mapping[code]

    print('{}\t{}'.format(name, degree))
