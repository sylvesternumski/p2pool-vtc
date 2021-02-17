**P2pool installation with pypy -- Windows**


On Windows, pypy is only supported via the Windows Subsystem for Linux (WSL). P2pool on pypy on WSL is much faster than P2pool on
CPython on native Windows. To install WSL, first follow the steps outlined here:


https://msdn.microsoft.com/en-us/commandline/wsl/install_guide


Once you've done that, run bash and follow the rest of the steps below.


**P2pool installation with pypy -- Linux and Windows**


Copy and paste the following commands into a bash shell in order to install p2pool on Windows or Linux.

>sudo apt-get update

>sudo apt-get install pypy pypy-dev pypy-setuptools gcc build-essential git


>wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo pypy
>sudo rm setuptools-*.zip


>wget https://files.pythonhosted.org/packages/84/21/80cdc749908ebf2719a9063eddcc02b668fbc62d200c1f1a4d92aaaba76b/zope.interface-5.2.0.tar.gz
tar zxf zope.interface-5.2.0.tar.gz

>cd zope.interface-5.2.0/

>sudo pypy setup.py install

>cd ..

>sudo rm -r zope.interface-5.2.0*


>wget https://files.pythonhosted.org/packages/4a/b4/4973c7ccb5be2ec0abc779b7d5f9d5f24b17b0349e23240cfc9dc3bd83cc/Twisted-20.3.0.tar.bz2

>tar jxf Twisted-20.3.0.tar.bz2

>cd Twisted-20.3.0

>sudo pypy setup.py install

>cd ..

>sudo rm -r Twisted-20.3.0*


>git clone https://github.com/vertcoin-project/p2pool-vtc


You'll also need to install and run your vertcoind, and edit ~/.vertcoin/vertcoin.conf with your vertcoind's RPC username and password. Launch your vertcoind, and after it has finished downloading blocks and syncing, go to your p2pool directory and run


>pypy run_p2pool.py


**Miner setup**


P2pool communicates with miners via the stratum protocol. For VTC, configure your miners with the following information:


>URL: stratum+tcp://(Your node's IP address or hostname):9171

>Worker: (Your bitcoin address)

>Password: x


For Litecoin, replace 9332 with 9327. For Bitcoin Cash, use 9348.


Mining to Legacy (P2PKH), SegWit/MultiSig (P2SH) and Bech32 addresses are supported for the following coins with the specified address prefixes:

|Coin		|P2PKH	|P2SH	|Bech32				|
|---------------|-------|-------|-------------------------------|
|Vertcoin	|`V...`	|`3...`	|`vtc...`			|


If you wish to modify the mining difficulty, you may add something like "address+1" after your mining address to set the pseudoshare difficulty to 1, or "address/10" to set the actual share difficulty to 10 or the p2pool minimum share difficulty, whichever is higher. Pseudoshares only affect hashrate statistics, whereas actual shares affect revenue variance and efficiency.


**Firewall considerations**


If your node is behind a firewall or behind NAT (i.e. on a private IP address), you may want to forward ports to your p2pool server. P2pool uses two ports: one for p2p communication with the p2pool network, and another for both the web UI and for stratum communication with workers. For Vertcoin, those ports are 9346 (p2p) and 9171 (stratum/web). 
