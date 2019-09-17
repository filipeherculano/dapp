import matplotlib.pyplot as plt
import numpy as np

def plot_data(path):
    data = []
    storage_size = open(path, 'r')
    while True:
        line = storage_size.readline()
        if line == '':
            break
        timestamp, elapsed_time = line.split(' ')
        data.append([float(timestamp), float(elapsed_time)])
    storage_size.close()

    data.sort()

    x = [v[0] for v in data] # elapsed time
    y = [v[1] for v in data] # time to block

    x[:] = [v - min(x) for v in x]
    x[:] = [v / 60.0 for v in x]
    y_ = [np.mean(y[0:i]) for i in range(0, len(y))]

    plt.bar(x, y)
    plt.plot(x, y_, 'r.')
    plt.show()

def main():
    # Insert new plotting files here
    files = ["slow_storage_tx_time_store.txt", "slow_storage_tx_time_retrieve.txt"]
    for file in files:
        plot_data("build/plot_data/" + file);

if __name__ == '__main__':
    main()
