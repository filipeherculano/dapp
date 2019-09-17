#!/usr/bin/env python

import os
import sys

paths = []

if sys.argv[1] == "":
    paths.append("test/SlowStorageTest.js")
elif sys.argv[1] == "ipfs":
    paths.append("test/FastStorageIPFS.js")
else:
    sys.exit("Unknown parameters")

os.system("python3 scripts/python/start_timer.py " + sys.argv[1] + " &")   # watch time x storage in 10 secs

os.system("sleep 15")
os.system("node " + paths[0])

os.system("kill -9 $(sudo ps -efo pid,cmd | grep start_timer.py | grep python | awk '{print $1}')")
