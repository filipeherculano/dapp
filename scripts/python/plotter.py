import matplotlib.pyplot as plt
import numpy as np

def plot_data(path, title):
    data = []
    storage_size = open(path, 'r')
    while True:
        line = storage_size.readline()
        if line == '':
            break
        size, elapsed_time = line.split(' ')
        data.append([int(size, 10), float(elapsed_time)])
    storage_size.close()

    data.sort()

    x = [v[0] for v in data] # size (Kb)
    y = [v[1] for v in data] # time to block (seconds)

    y[:] = [v - min(y) for v in y]
    y[:] = [v / 1000.0 for v in y]
    y_ = [np.mean(y[0:i]) for i in range(0, len(y))]

    plt.plot(x, y, 'r.')
    plt.xlabel('data size (Kb)')
    plt.ylabel('time (s)')
    plt.title(title)

    plt.show()

def main():
    # Insert new plotting files here
    files = ["slow_storage_tx_time_store.txt", "slow_storage_tx_time_retrieve.txt"]
    titles = ["Slow Storage time given data size", "Slow Retrieve time given data size"]
    for i in range(0, len(files)):
        plot_data("build/plot_data/" + files[i], titles[i]);

if __name__ == '__main__':
    main()
