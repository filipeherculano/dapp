import matplotlib.pyplot as plt
import numpy as np
import os

# size of the transaction influences time to transaction in block
def size_to_elapsed(path, title, xl, yl):
    if(os.path.isfile(path) == False):
        return

    data = []
    spent = []
    storage_size = open(path, 'r')
    while True:
        line = storage_size.readline()
        if line == '':
            break
        arr = line.split(' ')
        elapsed_time = arr[2]
        if len(arr) == 5:
            gas = arr[4]
            spent.append(int(gas, 10))
        data.append(float(elapsed_time))
    storage_size.close()

    print("{}: {}".format(title, np.mean(data)))
    print("Gasto médio de unidades de gás: {}".format(np.mean(spent)))
    plt.hist(data, ec='black')
    plt.xlabel(xl)
    plt.ylabel(yl)
#    plt.title(title)

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
        size, start, elapsed_time, block, spent = line.split(' ')
        data.append(int(block, 10))
    storage_size.close()

    x, y = np.unique(np.array(data), return_counts=True)

    print("{}: {}".format(title, np.mean(y)))
    plt.bar(x, y, ec='black')
    plt.xlabel(xl)
    plt.ylabel(yl)
#    plt.title(title)
#    plt.ylim(0,60)

    plt.show()

def main():
    # Insert new plotting files here
    tests = ["SlowStorage", "FastStorageIPFS", "FastStorageSWARM"]
    ids = {
        "SlowStorage": {
            "SlowStorage_store.txt" : [
                ["Frequência de Tempo de Publicação em Slow Storage Store", "Tempo de Publicação em Bloco (s)", "Frequência"],
                ["Número de Transações por Bloco Slow Storage Store", "Número do Bloco", "Número de Transações"]
            ],
            "SlowStorage_retrieve.txt" : [
                ["Frequência de Tempo de Publicação em Slow Storage Retrieve", "Tempo de Publicação em Bloco (s)", "Frequência"],
            ]
        },
        "FastStorageIPFS": {
            "FastStorageIPFS_store.txt" : [
                ["Frequência de Tempo de Publicação em Fast Storage Store", "Tempo de Publicação em Bloco (s)", "Frequência"],
                ["Número de Transações por Bloco Fast Storage Store", "Número do Bloco", "Número de Transações"]
            ],
            "FastStorageIPFS_retrieve.txt" : [
                ["Frequência de Tempo de Publicação em Fast Storage Retrieve", "Tempo de Busca (s)", "Frequência"],
            ]
        },
        "FastStorageSWARM": {
            "FastStorageSWARM_store.txt" : [
                ["Frequência de Tempo de Publicação em Fast Storage Store", "Tempo de Publicação em Bloco (s)", "Frequência"],
                ["Número de Transações por Bloco Fast Storage Store", "Número do Bloco", "Número de Transações"]
            ],
            "FastStorageSWARM_retrieve.txt" : [
                ["Frequência de Tempo de Publicação em Fast Storage Retrieve", "Tempo de Busca (s)", "Frequência"],
            ]
        }
    }

    for test in tests:
        store_file = test + "_store.txt"
        retrieve_file = test + "_retrieve.txt"
        size_to_elapsed("build/plot_data/" + test + "_store.txt", test + " " + ids[test][store_file][0][0],ids[test][store_file][0][1], ids[test][store_file][0][2])
        tx_per_block("build/plot_data/" + test + "_store.txt", test + " " + ids[test][store_file][1][0], ids[test][store_file][1][1], ids[test][store_file][1][2])
        size_to_elapsed("build/plot_data/" + test + "_retrieve.txt", test + " " + ids[test][retrieve_file][0][0], ids[test][retrieve_file][0][1], ids[test][retrieve_file][0][2])

if __name__ == '__main__':
    main()
