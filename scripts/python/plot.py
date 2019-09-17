#!/usr/bin/env python

import os

os.system("node scripts/js/get_times.js")
#os.system("rm buffer.txt")
os.system("python3 scripts/python/plotter.py")
os.system("python3 scripts/python/plotter_size.py")
