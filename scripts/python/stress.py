import os
import subprocess
import sys
import time

#sizes = [1, 10, 100, 1000, 1000000]
sizes = [1, 10, 100, 1000, 1000000]

def ipfs():
    for size in sizes:
        for i in range(1):
            f = open("img.bin","w+b")
            f.write(bytearray(os.urandom(size)))
            f.close()

            before = time.time()
            out = subprocess.check_output("ipfs add img.bin", shell=True).split()[1].decode('utf-8')
            after = time.time()
            print(after - before)

            before = time.time()
            out = subprocess.check_output("ipfs get " + out, shell=True)
            after = time.time()
            print(after - before)


def main(param):
    if param == "ipfs":
        ipfs()
    elif param == "sia":
        ipfs()
    elif param == "swarm":
        ipfs()
    elif param == "storj":
        ipfs()
    else :
        print("Invalid Parameter")

if __name__ == "__main__":
    print(sys.argv[1])
    main(sys.argv[1])
