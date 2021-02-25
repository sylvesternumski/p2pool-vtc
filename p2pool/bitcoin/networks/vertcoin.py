import os
import platform
import hashlib

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

import verthash

def verthash_hash(dat):
    return verthash.getPoWHash(dat)


P2P_PREFIX='fabfb5da'.decode('hex')
P2P_PORT=5889
ADDRESS_VERSION=71
SEGWIT_ADDRESS_VERSION=5
RPC_PORT=5888
RPC_CHECK=lambda bitcoind: True
SUBSIDY_FUNC=lambda height: 50*100000000 >> (height + 1)//840000
POW_FUNC=lambda data: pack.IntType(256).unpack(verthash_hash(data))
BLOCK_PERIOD=150 # s
SYMBOL='VTC'
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Vertcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Vertcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.vertcoin'), 'vertcoin.conf')
BLOCK_EXPLORER_URL_PREFIX='http://insight.vertcoin.org/block/'
ADDRESS_EXPLORER_URL_PREFIX='http://insight.vertcoin.org/address/'
TX_EXPLORER_URL_PREFIX='http://insight.vertcoin.org/tx/'
SANE_TARGET_RANGE=(2**256//1000000000000000000 - 1, 2**256//100000 - 1)
DUMB_SCRYPT_DIFF=16
DUST_THRESHOLD=0.03e8
HUMAN_READABLE_PART = 'vtc'
