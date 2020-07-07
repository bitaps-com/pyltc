import pybtc.functions.key as __parent__
from  pybtc.functions.key import private_key_to_wif as _private_key_to_wif


import types
import functools

def copy_func(f):
    """Based on http://stackoverflow.com/a/6528148/190597 (Glenn Maynard)"""
    g = types.FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__,  closure=f.__closure__)
    g = functools.update_wrapper(g, f)
    g.__kwdefaults__ = f.__kwdefaults__
    return g

private_key_to_wif = copy_func(__parent__.private_key_to_wif)

from pyltc.constants import  *
# names = getattr(constants, '__all__', [n for n in dir(constants) if not n.startswith('_')])
# [setattr(__parent__, name, getattr(constants, name)) for name in names]


def create_private_key(compressed=True, testnet=False, wif=True, hex=False):
    """
    Create private key

    :param compressed: (optional) Type of public key, by default set to compressed.
                                 Using uncompressed public keys is deprecated in new SEGWIT addresses,
                                 use this option only for backward compatibility.
    :param testnet: (optional) flag for testnet network, by default is False.
    :param wif:  (optional) If set to True return key in WIF format, by default is True.
    :param hex:  (optional) If set to True return key in HEX format, by default is False.
    :return: Private key in wif format (default), hex encoded byte string in case of hex flag or
             raw bytes string in case wif and hex flags set to False.

    """
    return __parent__.create_private_key(compressed=compressed, testnet=testnet, wif=wif, hex=hex)



# def private_key_to_wif(h, compressed=True, testnet=False):
#     """
#     Encode private key in HEX or RAW bytes format to WIF format.
#
#     :param h: private key 32 byte string or HEX encoded string.
#     :param compressed: (optional) flag of public key compressed format, by default set to True.
#     :param testnet: (optional) flag for testnet network, by default is False.
#     :return: Private key in WIF format.
#     """
#     # uncompressed: 0x80 + [32-byte secret] + [4 bytes of Hash() of previous 33 bytes], base58 encoded.
#     # compressed: 0x80 + [32-byte secret] + 0x01 + [4 bytes of Hash() previous 34 bytes], base58 encoded.
#     return _private_key_to_wif(h, compressed=compressed, testnet=testnet)


def wif_to_private_key(h, hex=True):
    """
    Decode WIF private key to bytes string or HEX encoded string

    :param hex:  (optional) if set to True return key in HEX format, by default is True.
    :return: Private key HEX encoded string or raw bytes string.
    """
    return __parent__.wif_to_private_key(h, hex=hex)


def is_wif_valid(wif):
    """
    Check is private key in WIF format string is valid.

    :param wif: private key in WIF format string.
    :return: boolean.
    """
    return __parent__.is_wif_valid(wif)


def private_to_public_key(private_key, compressed=True, hex=True):
    """
    Get public key from private key using ECDSA secp256k1

    :param private_key: private key in WIF, HEX or bytes.
    :param compressed: (optional) flag of public key compressed format, by default set to True.
                       In case private_key in WIF format, this flag is set in accordance with
                       the key format specified in WIF string.
    :param hex:  (optional) if set to True return key in HEX format, by default is True.
    :return: 33/65 bytes public key in HEX or bytes string.
    """
    return __parent__.private_to_public_key(private_key, compressed=compressed, hex=hex)


def is_public_key_valid(key):
    """
    Check public key is valid.

    :param key: public key in HEX or bytes string format.
    :return: boolean.
    """
    return __parent__.is_public_key_valid(key)


