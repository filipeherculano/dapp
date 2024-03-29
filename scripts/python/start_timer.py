#!/usr/bin/env python

import os
import sys

arg = (sys.argv[1] if len(sys.argv) >= 2 else "")
paths = ["SlowStorage_size.txt","FastStorageIPFS_size.txt","FastStorageSWARM_size.txt","FastStorageSIA_size.txt"]
arg_to_int = {"":0,"ipfs":1,"swarm":2,"sia":3}

os.system("sleep 12")
while(1):
    os.system("mkdir -p build/plot_data/")
    os.system("touch build/plot_data/"+ paths[arg_to_int[arg]])
    os.system("date +%s >> build/plot_data/"+ paths[arg_to_int[arg]])
    os.system("du -h --block-size=1K build/chain/ >> build/plot_data/"+ paths[arg_to_int[arg]])
    os.system("sleep 3")
