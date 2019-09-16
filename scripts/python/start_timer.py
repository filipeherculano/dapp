#!/usr/bin/env python

import os

os.system("sleep 10")
while(1):
    os.system("mkdir -p build/plot_data/")
    os.system("touch build/plot_data/slow_storage_size.txt")
    os.system("date +%s >> build/plot_data/slow_storage_size.txt")
    os.system("du -h build/chain/ >> build/plot_data/slow_storage_size.txt")
    os.system("sleep 1")
