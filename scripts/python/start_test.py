#!/usr/bin/env python

import os

os.system("sudo python3 scripts/python/start_timer.py &")   # watch time x storage in 10 secs

os.system("sleep 15")
os.system("sudo node test/SlowStorageTest.js")

os.system("sudo kill -9 $(sudo ps -efo pid,cmd | grep start_test.py | grep python | awk '{print $1}')")
