#!/usr/bin/env python

import os
import sys

arg = (sys.argv[1] if len(sys.argv) >= 2 else "")
paths = ["SlowStorage_","FastStorageIPFS_","FastStorageSWARM","FastStorageSIA"]
arg_to_int = {"":0,"ipfs":1,"swarm":2,"sia":3}

if arg == "chain":
    os.system("rm -rf build/chain/")
else :
    os.system("rm -rf build/plot_data/" + paths[arg_to_int[arg]] + "*")
