#!/usr/bin/env python

import os
import sys

arg = (sys.argv[1] if len(sys.argv) >= 2 else "")

os.system("mkdir -p build/chain/")
os.system("python3 scripts/python/start_timer.py " + arg + " &")   # watch time x storage in 12 secs
os.system("python3 scripts/python/start_test.py " + arg + " &")    # start simulation in 10 secs

os.system("ganache-cli -g 22000000000 -l 8000000 -e 1000000000000000 -a 1000 -b 12 -i 5777 -p 7545 --db build/chain/") # start chain

os.system("kill -9 $(ps -efo pid,cmd | grep start_timer.py | grep python | awk '{print $1}')")
os.system("kill -9 $(ps -efo pid,cmd | grep start_test.py | grep python | awk '{print $1}')")

os.system("rm *buffer.txt")
