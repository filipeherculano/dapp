import matplotlib.pyplot as plt
import numpy as np

def plot_data(path):
    data = []
    storage_size = open(path, 'r')
    while True:
        timestamp = storage_size.readline()
        line = storage_size.readline()
        if line == '':
            break
        size = line.split('M')
        data.append([float(timestamp), float(size[0])])
    storage_size.close()

    data.sort()

    x = [v[0] for v in data] # elapsed time
    y = [v[1] for v in data] # memory usage

    x[:] = [v - min(x) for v in x]
    x[:] = [v / 60.0 for v in x]

    plt.plot(x, y, 'r.')
    plt.show()

def main():
    # Insert new plotting files here
    files = ["slow_storage_size.txt"]
    for file in files:
        plot_data("build/plot_data/" + file);

if __name__ == '__main__':
    main()
