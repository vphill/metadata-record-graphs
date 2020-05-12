import fileinput
import statistics
import numpy as np
from scipy import stats

degree_data = []

for line in fileinput.input():
    line = line.strip()
    identifier, degree = line.split('\t')
    degree_data.append(int(degree))

if degree_data:
    m, c = stats.mode(degree_data)
    mode = m[0]
    mode_frequency = c[0] / len(degree_data)
    print('N', len(degree_data))
    print('min:', min(degree_data))
    print('q1:', int(np.percentile(degree_data, 25)))
    print('median:', int(statistics.median(degree_data)))
    print('q3:', int(np.percentile(degree_data, 75)))
    print('max:', max(degree_data))
    print('mean: {0:0.1f}'.format(statistics.mean(degree_data)))
    print('stddev: {0:0.1f}'.format(statistics.stdev(degree_data)))
    print('mode:', mode)
    print('mode frequency: {0:0.4f}'.format(mode_frequency))
else:
    print(0)