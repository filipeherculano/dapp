#!/usr/bin/env python

import os
import sys

arg = (sys.argv[1] if len(sys.argv) >= 2 else "")
paths = ["test/SlowStorageTest.js","test/FastStorageIPFS.js", "test/FastStorageSWARM.js"]
arg_to_int = {"":0,"ipfs":1,"swarm":2}

os.system("sleep 10")
os.system("node " + paths[arg_to_int[arg]])
