#!/usr/bin/env python

import os
import sys

paths = []

if sys.argv[1] == "":
    paths.append("SlowStorageTest.txt")
elif sys.argv[1] == "ipfs":
    paths.append("FastStorageIPFS.txt")
else:
    sys.exit("Unknown parameters")

os.system("sleep 15")
while(1):
    os.system("mkdir -p build/plot_data/")
    os.system("touch build/plot_data/"+ paths[0])
    os.system("date +%s >> build/plot_data/"+ paths[0])
    os.system("du -h build/chain/ >> build/plot_data/"+ paths[0])
    os.system("sleep 5")
