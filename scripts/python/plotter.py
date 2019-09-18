import matplotlib.pyplot as plt
import numpy as np
import os

# size of the transaction influences time to transaction in block
def size_to_elapsed(path, title, xl, yl):
    if(os.path.isfile(path) == False):
        return

    data = []
    storage_size = open(path, 'r')
    while True:
        line = storage_size.readline()
        if line == '':
            break
        size, start, elapsed_time, block = line.split(' ')
        data.append([int(size, 10), float(elapsed_time)])
    storage_size.close()

    x = [v[0] for v in data] # size (Kb)
    y = [v[1] for v in data] # time to block (seconds)

    y[:] = [v - min(y) for v in y]
    y[:] = [v / 1000.0 for v in y]

    plt.plot(x, y, 'r.')
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.title(title)

    plt.show()

# test time influences time to transaction in block
def time_to_elapsed(path, title, xl, yl):
    if(os.path.isfile(path) == False):
        return

    data = []
    storage_size = open(path, 'r')
    while True:
        line = storage_size.readline()
        if line == '':
            break
        size, start, elapsed_time, block = line.split(' ')
        data.append([float(start), float(elapsed_time)])
    storage_size.close()

    x = [v[0] for v in data] # elapsed test time (seconds)
    y = [v[1] for v in data] # time to block (seconds)

    x[:] = [v - min(x) for v in x]
    x[:] = [v / 1000.0 for v in x]

    plt.plot(x, y, 'r.')
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.title(title)

    plt.show()

def main():
    # Insert new plotting files here
    tests = ["SlowStorage", "FastStorageIPFS"]
    ids = {
        "SlowStorage": {
            "SlowStorage_store.txt" : [
                ["Slow Storage Store", "Transaction Size (Kb)", "Time To Block (s)"],
                ["Slow Storage Store", "Elapsed Test Time (s)", "Time To Block (s)"]
            ],
            "SlowStorage_retrieve.txt" : [
                ["Slow Storage Retrieve", "Transaction Size (Kb)", "Time To Block (s)"],
                ["Slow Storage Retrieve", "Elapsed Test Time (s)", "Time To Block (s)"]
            ]
        },
        "FastStorageIPFS": {
            "FastStorageIPFS_store.txt" : [
                ["Fast Storage Store", "Transaction Size (Kb)", "Time To Block (s)"],
                ["Fast Storage Store", "Elapsed Test Time (s)", "Time To Block (s)"]
            ],
            "FastStorageIPFS_retrieve.txt" : [
                ["Fast Storage Retrieve", "Transaction Size (Kb)", "Time To Block (s)"],
                ["Fast Storage Retrieve", "Elapsed Test Time (s)", "Time To Block (s)"]
            ]
        }
    }

    for test in tests:
        for i in range(2):
            size_to_elapsed("build/plot_data/" + test + "_store.txt", ids[test][test + "_store.txt"][i][0], ids[test][test + "_store.txt"][i][1], ids[test][test + "_store.txt"][i][2])
            time_to_elapsed("build/plot_data/" + test + "_retrieve.txt", ids[test][test + "_retrieve.txt"][i][0], ids[test][test + "_retrieve.txt"][i][1], ids[test][test + "_retrieve.txt"][i][2])

if __name__ == '__main__':
    main()
