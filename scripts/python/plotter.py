import matplotlib.pyplot as plt

x = []
y = []

storage_size = open("build/plot_data/slow_storage_tx_time_store.txt", 'r')
while True:
    line = storage_size.readline()
    if line == '':
        break
    timestamp, elapsed_time = line.split(' ')
    x.append(timestamp)
    y.append(elapsed_time)
storage_size.close()

plt.plot(x, y, 'ro')
plt.show()
