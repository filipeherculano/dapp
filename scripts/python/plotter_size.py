import matplotlib.pyplot as plt
import numpy as np

def plot_data(path, title):
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

    x = [v[0] for v in data] # elapsed time (seconds)
    y = [v[1] for v in data] # memory usage

    x[:] = [v - min(x) for v in x]

    plt.plot(x, y, 'r.')
    plt.ylabel('data size (Mb)')
    plt.xlabel('time (s)')
    plt.title(title)

    plt.show()

def main():
    # Insert new plotting files here
    files = ["slow_storage_size.txt"]
    titles = ["Slow Storage Blockchain Size"]
    for i in range(0, len(files)):
        plot_data("build/plot_data/" + files[i], titles[i]);

if __name__ == '__main__':
    main()
