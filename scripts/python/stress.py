import os
import subprocess
import sys
import time

rounds = 10
sizes = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]

def ipfs():
    res = []

    for size in sizes:
        med_store = 0.0
        med_ret = 0.0

        for i in range(rounds):
            os.system("ipfs init")

            f = open("img.bin","w+b")
            f.write(bytearray(os.urandom(size)))
            f.close()

            before = time.time()
            out = subprocess.check_output("ipfs add img.bin", shell=True).split()[1].decode('utf-8')
            after = time.time()
            med_store = med_store + (after - before)

            before = time.time()
            os.system("ipfs get " + out)
            after = time.time()
            med_ret = med_ret + (after - before)

            os.system("sudo rm " + out)
            os.system("sudo rm -rf ~/.ipfs")

        med_store = med_store / float(rounds)
        med_ret = med_ret / float(rounds)
        res.append([med_store, med_ret])

    for i in range(len(res)):
        print("MEDIAN OF STORE TIME ON SIZE {} IS {}".format(sizes[i], res[i][0]))
        print("MEDIAN OF RETRIEVE TIME ON SIZE {} IS {}".format(sizes[i], res[i][1]))

def sia():
    print("NOT IMPLEMENTED")

def swarm():
    res = []

    for size in sizes:
        med_store = 0.0
        med_ret = 0.0

        for i in range(rounds):
            print("TESTING ROUND {} WITH SIZE {}".format(i, size))
            os.system("echo 11316652 | swarm init &")
            time.sleep(2)
            f = open("img.bin","w+b")
            f.write(bytearray(os.urandom(size)))
            f.close()

            before = time.time()
            out = subprocess.check_output("swarm up img.bin", shell=True).decode('utf-8')
            after = time.time()
            med_store = med_store + (after - before)

            before = time.time()
            os.system("swarm down bzz:/" + out)
            after = time.time()
            med_ret = med_ret + (after - before)

            os.system("sudo rm " + out)
            os.system("kill -9 $(ps aux | grep swarm | grep init | awk '{print $2}')")
            os.system("sudo rm -rf ~/.ethereum/swarm")

        med_store = med_store / float(rounds)
        med_ret = med_ret / float(rounds)
        res.append([med_store, med_ret])

    for i in range(len(res)):
        print("MEDIAN OF STORE TIME ON SIZE {} IS {}".format(sizes[i], res[i][0]))
        print("MEDIAN OF RETRIEVE TIME ON SIZE {} IS {}".format(sizes[i], res[i][1]))

def storj():
    print("NOT IMPLEMENTED")

def main(param):
    if param == "ipfs":
        ipfs()
    elif param == "sia":
        sia()
    elif param == "swarm":
        swarm()
    elif param == "storj":
        storj()
    else :
        print("Invalid Parameter")

if __name__ == "__main__":
    main(sys.argv[1])
