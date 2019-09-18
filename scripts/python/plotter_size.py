import matplotlib.pyplot as plt
import numpy as np
import os

def time_to_size(path, title, xl, yl):
    if(os.path.isfile(path) == False):
        return

    data = []
    storage_size = open(path, 'r')
    while True:
        timestamp = storage_size.readline()
        line = storage_size.readline()
        if line == '':
            break

        if(len(line.split('K')) != 1):
            size = line.split('K')
            size = size[0].replace(",", ".")
            data.append([float(timestamp), float(size)/1000.0])
        elif(len(line.split('M')) != 1):
            size = line.split('M')
            size = size[0].replace(",", ".")
            data.append([float(timestamp), float(size)])
        elif(len(line.split('G')) != 1):
            size = line.split('G')
            size = size[0].replace(",", ".")
            data.append([float(timestamp), float(size)*1000.0])
    storage_size.close()

    x = [v[0] for v in data] # elapsed test time (seconds)
    y = [v[1] for v in data] # memory usage (Mb)

    x[:] = [v - min(x) for v in x]

    plt.plot(x, y, 'r.')
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.title(title)

    plt.show()

def main():
    # Insert new plotting files here
    tests = ["SlowStorage", "FastStorageIPFS"]
    ids = {
        "SlowStorage": ["Slow Storage Blockchain size", "Elapsed Test Time (s)", "Memory Usage (Mb)"],
        "FastStorageIPFS": ["Fast Storage Blockchain size", "Elapsed Test Time (s)", "Memory Usage (Mb)"]
    }

    for test in tests:
        title = ids[test][0]
        xlabel = ids[test][1]
        ylabel = ids[test][2]
        time_to_size("build/plot_data/" + test + "_size.txt",title, xlabel, ylabel)

if __name__ == '__main__':
    main()
