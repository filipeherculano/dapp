#!/usr/bin/env python

import os

os.system("sudo mkdir -p build/chain/")

os.system("sudo python3 scripts/python/start_test.py &")    # start simulation in 10 secs

os.system("sudo ganache-cli -g 22000000000 -l 8000000 -e 100000000000000000 -a 1000 -b 11 -i 5777 -p 7545 --db build/chain/") # start chain

os.system("sudo kill -9 $(sudo ps -efo pid,cmd | grep start_timer.py | grep python | awk '{print $1}')")
