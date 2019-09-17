#!/usr/bin/env python

import os
import sys

os.system("mkdir -p build/chain/")
os.system("python3 scripts/python/start_test.py " + sys.argv[1] + " &")    # start simulation in 15 secs
os.system("ganache-cli -g 22000000000 -l 8000000 -e 100000000000000000 -a 1000 -b 11 -i 5777 -p 7545 --db build/chain/") # start chain
os.system("kill -9 $(sudo ps -efo pid,cmd | grep start_test.py | grep python | awk '{print $1}')")
