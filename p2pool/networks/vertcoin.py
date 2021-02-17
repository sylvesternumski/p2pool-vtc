from p2pool.bitcoin import networks

PARENT = networks.nets['vertcoin']
SHARE_PERIOD = 30 
CHAIN_LENGTH=24*60*60//30 # shares
REAL_CHAIN_LENGTH=24*60*60//30 # shares
TARGET_LOOKBEHIND = 100 # shares
SPREAD = 12 # blocks
IDENTIFIER = '4B62545B1A631A5C'.decode('hex')
PREFIX = '1c0c1c71cc197bc1'.decode('hex')
P2P_PORT = 9346
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False # Set to False for solo mining or starting a new chain
WORKER_PORT = 9171
BOOTSTRAP_ADDRS = [
        'p2p-south.xyz',
        'p2p-ekb.xyz',
        'p2p-usa.xyz',
        'sha256.p2p-spb.xyz',
        ]
ANNOUNCE_CHANNEL = '#p2pool'
VERSION_CHECK = lambda v: True
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip34', 'bip66', 'bip65', 'csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 3501
SEGWIT_ACTIVATION_VERSION = 35
BLOCK_MAX_SIZE = 8000000
BLOCK_MAX_WEIGHT = 32000000
