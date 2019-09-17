# Installation

Clone project, enter folder then Install nodejs and npm.

```
git clone https://github.com/filipeherculano/dapp
cd dapp
sudo apt install nodejs npm python3-pip solc
```


```
sudo pip3 install matplotlib
```

Then install truffle framework with npm. But before it, create a truffle folder inside your ~/.config folder. So the installation can run smoothly...

```
mkdir ~/.config/truffle
```

Use sudo so the script can access your /usr/local/lib. Also, install ganache-cli, will use it to run our local Ethereum network. Then, install all project dependencies.


```
sudo npm install -g truffle ganache-cli
sudo npm install
```

This should take a while ...

install IPFS by downloading it from page, extracting it and running the script

https://dist.ipfs.io/#go-ipfs

tar xvfz go-ipfs.tar.gz
cd go-ipfs
./install.sh

=============================================================

ipfs init

ipfs daemon

ipfs swarm peers

ipfs add -r <folder>

# Usage

First you'll need to start the chain and all tests within. They will put their data onto buffer.txt and build/plot_data/*.txt. The buffer.txt will be used and deleted afterwords.

```
sudo python3 scripts/python/start_chain.py
sudo python3 scripts/python/plot.py
```

Make sure to run plot.py in another terminal, since you must still be running your local blockchain on ganache.
