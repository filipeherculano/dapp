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
        data.append(float(elapsed_time))
    storage_size.close()

    plt.hist(data, ec='black')
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.title(title)
    plt.ylim(0,100)

    plt.show()

def tx_per_block(path, title, xl, yl):
    if(os.path.isfile(path) == False):
        return

    data = []
    storage_size = open(path, 'r')
    while True:
        line = storage_size.readline()
        if line == '':
            break
        size, start, elapsed_time, block = line.split(' ')
        data.append(int(block, 10))
    storage_size.close()

    x, y = np.unique(np.array(data), return_counts=True)

    plt.bar(x, y, ec='black')
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.title(title)
    plt.ylim(0,60)

    plt.show()

def main():
    # Insert new plotting files here
    tests = ["SlowStorage", "FastStorageIPFS"]
    ids = {
        "SlowStorage": {
            "SlowStorage_store.txt" : [
                ["Frequência de Tempo de Publicação em Slow Storage Store", "Time to Block (s)", "Frequência"],
                ["Número de Transações por Bloco Slow Storage Store", "Block Number", "Number of Transactions"]
            ],
            "SlowStorage_retrieve.txt" : [
                ["Frequência de Tempo de Publicação em Slow Storage Retrieve", "time to block (s)", "Frequência"],
            ]
        },
        "FastStorageIPFS": {
            "FastStorageIPFS_store.txt" : [
                ["Frequência de Tempo de Publicação em Fast Storage Store", "Time to Block (s)", "Frequência"],
                ["Número de Transações por Bloco Fast Storage Store", "Block Number", "Number of Transactions"]
            ],
            "FastStorageIPFS_retrieve.txt" : [
                ["Frequência de Tempo de Publicação em Fast Storage Retrieve", "time to block (s)", "Frequência"],
            ]
        }
    }

    for test in tests:
        store_file = test + "_store.txt"
        retrieve_file = test + "_retrieve.txt"
        size_to_elapsed("build/plot_data/" + test + "_store.txt", ids[test][store_file][0][0], ids[test][store_file][0][1], ids[test][store_file][0][2])
        tx_per_block("build/plot_data/" + test + "_store.txt", ids[test][store_file][1][0], ids[test][store_file][1][1], ids[test][store_file][1][2])
        size_to_elapsed("build/plot_data/" + test + "_retrieve.txt", ids[test][retrieve_file][0][0], ids[test][retrieve_file][0][1], ids[test][retrieve_file][0][2])

if __name__ == '__main__':
    main()
