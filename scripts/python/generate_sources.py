#!/usr/bin/env python

import os

contracts = ["SlowStorage", "FastStorageIPFS", "FastStorageSWARM", "FastStorageSIA"]

os.system("rm -rf build/abi/ build/bin/")
os.system("mkdir -p build/abi/ build/bin/")

for contract in contracts:
    os.system("echo -n 0x > build/bin/" + contract + ".bin && solc --bin contracts/" + contract + ".sol | tail -1 >> build/bin/" + contract + ".bin")
    os.system("solc --abi contracts/" + contract + ".sol | tail -1 > build/abi/" + contract + ".abi")
