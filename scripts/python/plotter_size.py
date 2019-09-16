import matplotlib.pyplot as plt
import numpy as np

data = []

storage_size = open("build/plot_data/slow_storage_size.txt", 'r')
while True:
    timestamp = storage_size.readline()
    line = storage_size.readline()
    if line == '':
        break
    size = line.split('M')
    data.append([float(timestamp), float(size[0])])
storage_size.close()

data.sort()

x = [v[0] for v in data]
y = [v[1] for v in data]

x[:] = [v - min(x) for v in x]
x[:] = [v / 60.0 for v in x]

plt.plot(x, y, 'r.')
plt.show()
