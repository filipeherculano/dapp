# Instalation

Clone project, enter folder then Install nodejs and npm.

```
git clone https://github.com/filipeherculano/dapp
cd dapp
sudo apt install nodejs npm python-pip solc
```


```
sudo pip install matplotlib
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

then, go to Ganache website, download their latest appimage, give all users executable permission
chmod a+x ~/Downloads/Ganache-2.1.0.AppImage
sudo ./Downloads/Ganache-.1.0.AppImage

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
