import pybtc.functions.bip32 as __parent__
import pyltc.constants as constants
names = getattr(constants, '__all__', [n for n in dir(constants) if not n.startswith('_')])
[setattr(__parent__, name, getattr(constants, name)) for name in names]

import pyltc.opcodes as opcodes
names = getattr(opcodes, '__all__', [n for n in dir(opcodes) if not n.startswith('_')])
[setattr(__parent__, name, getattr(opcodes, name)) for name in names]


from pybtc.constants import *


def create_master_xprivate_key(seed, testnet=False, base58=True, hex=False):
    """
    Create extended private key from seed

    :param str,bytes key: seed HEX or bytes string.
    :param boolean base58: (optional) return result as base58 encoded string, by default True.
    :param boolean hex: (optional) return result as HEX encoded string, by default False.
                        In case True base58 flag value will be ignored.
    :return: extended private key  in base58, HEX or bytes string format.
    """
    return __parent__.create_master_xprivate_key(seed, testnet=testnet, base58=base58, hex=hex)


def xprivate_to_xpublic_key(xprivate_key, base58=True, hex=False):
    """
    Get extended public key from extended private key using ECDSA secp256k1

    :param str,bytes key: extended private key in base58, HEX or bytes string.
    :param boolean base58: (optional) return result as base58 encoded string, by default True.
    :param boolean hex: (optional) return result as HEX encoded string, by default False.
                        In case True base58 flag value will be ignored.
    :return: extended public key  in base58, HEX or bytes string format.
    """
    return __parent__.xprivate_to_xpublic_key(xprivate_key, base58=base58, hex=hex)


def derive_xkey(xkey, *path_level, base58=True, hex=False):
    """
    Child Key derivation for extended private/public keys

    :param bytes xkey: extended private/public in base58, HEX or bytes string format.
    :param list path_level: list of derivation path levels. For hardened derivation use HARDENED_KEY flag.
    :param boolean base58: (optional) return result as base58 encoded string, by default True.
    :param boolean hex: (optional) return result as HEX encoded string, by default False.
                        In case True base58 flag value will be ignored.
    :return: extended child private/public key  in base58, HEX or bytes string format.
    """
    return __parent__.derive_xkey(xkey, *path_level, base58=base58, hex=hex)


def derive_child_xprivate_key(xprivate_key, i):
    return __parent__.derive_child_xprivate_key(xprivate_key, i)


def derive_child_xpublic_key(xpublic_key, i):
    return __parent__.derive_child_xpublic_key(xpublic_key, i)


def public_from_xpublic_key(xpublic_key, hex=True):
    """
    Get public key from extended public key

    :param bytes xpublic_key: extended public in base58, HEX or bytes string format.
    :param boolean base58: (optional) return result as base58 encoded string, by default True.
    :param boolean hex: (optional) return result as HEX encoded string, by default False.
                        In case True base58 flag value will be ignored.
    :return: public key  in HEX or bytes string format.
    """
    return __parent__.public_from_xpublic_key(xpublic_key, hex=hex)


def private_from_xprivate_key(xprivate_key, wif=True, hex=False):
    """
    Get private key from extended private key

    :param bytes xprivate_key: extended public in base58, HEX or bytes string format.
    :param boolean wif: (optional) return result as WIF format, by default True.
    :param boolean hex: (optional) return result as HEX encoded string, by default False.
                        In case True WIF flag value will be ignored.
    :return: private key  in HEX or bytes string format.
    """
    return __parent__.private_from_xprivate_key(xprivate_key, wif=wif, hex=hex)


def is_xprivate_key_valid(key):
    """
    Check the extended private key is valid according to BIP-0032.

    :param key: extended private key in BASE58, HEX or bytes string format.
    :return: boolean.
    """
    return __parent__.is_xprivate_key_valid(key)


def is_xpublic_key_valid(key):
    """
    Check the extended private key is valid according to BIP-0032.

    :param key: extended private key in BASE58, HEX or bytes string format.
    :return: boolean.
    """
    return __parent__.is_xpublic_key_valid(key)