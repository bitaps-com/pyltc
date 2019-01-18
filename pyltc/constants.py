from secp256k1 import lib as secp256k1
import random
import os

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
BIP0039_DIR = os.path.normpath(os.path.join(ROOT_DIR, 'bip39_word_list'))

MAX_AMOUNT = 2100000000000000
SIGHASH_ALL = 0x00000001
SIGHASH_NONE = 0x00000002
SIGHASH_SINGLE = 0x00000003
SIGHASH_ANYONECANPAY = 0x00000080
ECDSA_SEC256K1_ORDER = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141


# mainnet
MAINNET_PRIVATE_KEY_BYTE_PREFIX = b'\xb0'

MAINNET_PRIVATE_KEY_UNCOMPRESSED_PREFIX = '6'
MAINNET_PRIVATE_KEY_COMPRESSED_PREFIX = 'T'


MAINNET_SEGWIT_ADDRESS_PREFIX = 'ltc'
MAINNET_ADDRESS_PREFIX = 'L'
MAINNET_SCRIPT_ADDRESS_LEGACY_PREFIX = '3'
MAINNET_SCRIPT_ADDRESS_PREFIX = 'M'

MAINNET_ADDRESS_BYTE_PREFIX = b'\x30'
MAINNET_SCRIPT_ADDRESS_BYTE_LEGACY_PREFIX = b'\x05'
MAINNET_SCRIPT_ADDRESS_BYTE_PREFIX = b'\x32'
MAINNET_SEGWIT_ADDRESS_BYTE_PREFIX = b'\x03\x03\x03\x00\x0c\x14\x03'


# testnet

TESTNET_PRIVATE_KEY_BYTE_PREFIX = b'\xef'

TESTNET_PRIVATE_KEY_UNCOMPRESSED_PREFIX = '9'
TESTNET_PRIVATE_KEY_COMPRESSED_PREFIX = 'c'

TESTNET_SEGWIT_ADDRESS_PREFIX = 'tltc'
TESTNET_ADDRESS_PREFIX = 'm'
TESTNET_ADDRESS_PREFIX_2 = 'n'

TESTNET_SCRIPT_ADDRESS_LEGACY_PREFIX = '2'
TESTNET_SCRIPT_ADDRESS_PREFIX = 'Q'


TESTNET_ADDRESS_BYTE_PREFIX = b'\x6f'
TESTNET_SCRIPT_ADDRESS_LEGACY_BYTE_PREFIX = b'\xc4'
TESTNET_SCRIPT_ADDRESS_BYTE_PREFIX = b'\x3a'
TESTNET_SEGWIT_ADDRESS_BYTE_PREFIX = b'\x03\x03\x03\x03\x00\x14\x0c\x14\x03'








ADDRESS_PREFIX_LIST = (MAINNET_ADDRESS_PREFIX,
                       TESTNET_ADDRESS_PREFIX,
                       TESTNET_ADDRESS_PREFIX_2,
                       MAINNET_SCRIPT_ADDRESS_PREFIX,
                       MAINNET_SCRIPT_ADDRESS_LEGACY_PREFIX,
                       TESTNET_SCRIPT_ADDRESS_PREFIX)

PRIVATE_KEY_PREFIX_LIST = (MAINNET_PRIVATE_KEY_UNCOMPRESSED_PREFIX,
                           MAINNET_PRIVATE_KEY_COMPRESSED_PREFIX,
                           TESTNET_PRIVATE_KEY_UNCOMPRESSED_PREFIX,
                           TESTNET_PRIVATE_KEY_COMPRESSED_PREFIX)








EC_COMPRESSED = secp256k1.SECP256K1_EC_COMPRESSED
EC_UNCOMPRESSED = secp256k1.SECP256K1_EC_UNCOMPRESSED

FLAG_SIGN = secp256k1.SECP256K1_CONTEXT_SIGN
FLAG_VERIFY = secp256k1.SECP256K1_CONTEXT_VERIFY
ALL_FLAGS = FLAG_SIGN | FLAG_VERIFY
NO_FLAGS = secp256k1.SECP256K1_CONTEXT_NONE

HAS_RECOVERABLE = hasattr(secp256k1, 'secp256k1_ecdsa_sign_recoverable')
HAS_SCHNORR = hasattr(secp256k1, 'secp256k1_schnorr_sign')
HAS_ECDH = hasattr(secp256k1, 'secp256k1_ecdh')

ECDSA_CONTEXT_SIGN = secp256k1.secp256k1_context_create(FLAG_SIGN)
ECDSA_CONTEXT_VERIFY = secp256k1.secp256k1_context_create(FLAG_VERIFY)
ECDSA_CONTEXT_ALL = secp256k1.secp256k1_context_create(ALL_FLAGS)
secp256k1.secp256k1_context_randomize(ECDSA_CONTEXT_SIGN,
                                      random.SystemRandom().randint(0, ECDSA_SEC256K1_ORDER).to_bytes(32, byteorder="big"))

SCRIPT_TYPES = {"P2PKH":        0,
                "P2SH":         1,
                "PUBKEY":       2,
                "NULL_DATA":    3,
                "MULTISIG":     4,
                "P2WPKH":       5,
                "P2WSH":        6,
                "NON_STANDART": 7
                }


# CONSTANTS hierarchical deterministic wallets (HD Wallets)
MAINNET_XPRIVATE_KEY_PREFIX = b'\x04\x88\xAD\xE4'
MAINNET_XPUBLIC_KEY_PREFIX = b'\x04\x88\xB2\x1E'
TESTNET_XPRIVATE_KEY_PREFIX = b'\x04\x35\x83\x94'
TESTNET_XPUBLIC_KEY_PREFIX = b'\x04\x35\x87\xCF'
HARDENED_KEY = 0x80000000
FIRST_HARDENED_CHILD = 0x80000000
PATH_LEVEL_BIP0044 = [0x8000002C, 0x80000000, 0x80000000, 0, 0]
TESTNET_PATH_LEVEL_BIP0044 = [0x8000002C, 0x80000001, 0x80000000, 0, 0]

