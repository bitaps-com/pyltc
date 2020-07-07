import pybtc.functions.key as __parent__
from pyltc.functions.encode import encode_base58, decode_base58
from pyltc.functions.hash import double_sha256
from pyltc.functions.bip39_mnemonic import generate_entropy
bytes_from_hex = bytes.fromhex
from pybtc.crypto import __secp256k1_ec_pubkey_create__
from pyltc.constants import  *

from pyltc.functions.tools import copy_function

GLOBALS = globals()

_private_key_to_wif = copy_function(__parent__.private_key_to_wif, GLOBALS)
_create_private_key = copy_function(__parent__.create_private_key, GLOBALS)
_wif_to_private_key = copy_function(__parent__.wif_to_private_key, GLOBALS)
_is_wif_valid = copy_function(__parent__.is_wif_valid, GLOBALS)
_private_to_public_key = copy_function(__parent__.private_to_public_key, GLOBALS)
_is_public_key_valid = copy_function(__parent__.is_public_key_valid, GLOBALS)


def create_private_key(compressed=True, testnet=False, wif=None, hex=None):
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
    return _create_private_key(compressed=compressed, testnet=testnet, wif=wif, hex=hex)


def private_key_to_wif(h, compressed=True, testnet=False):
    """
    Encode private key in HEX or RAW bytes format to WIF format.

    :param h: private key 32 byte string or HEX encoded string.
    :param compressed: (optional) flag of public key compressed format, by default set to True.
    :param testnet: (optional) flag for testnet network, by default is False.
    :return: Private key in WIF format.
    """
    # uncompressed: 0x80 + [32-byte secret] + [4 bytes of Hash() of previous 33 bytes], base58 encoded.
    # compressed: 0x80 + [32-byte secret] + 0x01 + [4 bytes of Hash() previous 34 bytes], base58 encoded.
    return _private_key_to_wif(h, compressed=compressed, testnet=testnet)


def wif_to_private_key(h, hex=True):
    """
    Decode WIF private key to bytes string or HEX encoded string

    :param hex:  (optional) if set to True return key in HEX format, by default is True.
    :return: Private key HEX encoded string or raw bytes string.
    """
    return _wif_to_private_key(h, hex=hex)


def is_wif_valid(wif):
    """
    Check is private key in WIF format string is valid.

    :param wif: private key in WIF format string.
    :return: boolean.
    """
    return _is_wif_valid(wif)


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
    return _private_to_public_key(private_key, compressed=compressed, hex=hex)


def is_public_key_valid(key):
    """
    Check public key is valid.

    :param key: public key in HEX or bytes string format.
    :return: boolean.
    """
    return _is_public_key_valid(key)


