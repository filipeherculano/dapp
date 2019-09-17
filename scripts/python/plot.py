#!/usr/bin/env python

import os

os.system("sudo node scripts/js/get_times.js")
os.system("rm buffer.txt")
os.system("sudo python3 scripts/python/plotter.py")
os.system("sudo python3 scripts/python/plotter_size.py")
