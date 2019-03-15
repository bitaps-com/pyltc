import pybtc.functions.address as __parent__
import pyltc.constants as constants
names = getattr(constants, '__all__', [n for n in dir(constants) if not n.startswith('_')])
[setattr(__parent__, name, getattr(constants, name)) for name in names]

import pyltc.opcodes as opcodes
names = getattr(opcodes, '__all__', [n for n in dir(opcodes) if not n.startswith('_')])
[setattr(__parent__, name, getattr(opcodes, name)) for name in names]


from pyltc.constants import *
from pyltc.opcodes import *
from pyltc.functions.hash import double_sha256
from pyltc.functions.encode import (encode_base58,
                                    decode_base58,
                                    rebase_8_to_5,
                                    rebase_5_to_32,
                                    rebase_32_to_5,
                                    bech32_polymod,
                                    base32charset,
                                    base32charset_upcase)





def hash_to_address(address_hash, testnet=False, script_hash=False, witness_version=0, legacy=False):
    """
    Get address from public key/script hash. In case PUBKEY, P2PKH, P2PKH public key/script hash is SHA256+RIPEMD160,
    P2WSH script hash is SHA256.
    :param address_hash: public key hash or script hash in HEX or bytes string format.
    :param testnet: (optional) flag for testnet network, by default is False.
    :param script_hash: (optional) flag for script hash (P2SH address), by default is False.
    :param witness_version: (optional) witness program version, by default is 0, for legacy
                            address format use None.
    :return: address in base58 or bech32 format.
    """
    if isinstance(address_hash, str):
        address_hash = bytes.fromhex(address_hash)
    if not isinstance(address_hash, bytes):
        raise TypeError("address hash must be HEX encoded string or bytes")

    if not script_hash:
        if witness_version is None:
            if len(address_hash) != 20:
                raise ValueError("address hash length incorrect")
            if testnet:
                prefix = TESTNET_ADDRESS_BYTE_PREFIX
            else:
                prefix = MAINNET_ADDRESS_BYTE_PREFIX
            address_hash = prefix + address_hash
            address_hash += double_sha256(address_hash)[:4]
            return encode_base58(address_hash)
        else:
            if len(address_hash) not in (20, 32):
                raise ValueError("address hash length incorrect")

    if witness_version is None:
        if testnet:
            if not legacy:
                prefix = TESTNET_SCRIPT_ADDRESS_BYTE_PREFIX
            else:
                prefix = TESTNET_SCRIPT_ADDRESS_LEGACY_BYTE_PREFIX
        else:
            if not legacy:
                prefix = MAINNET_SCRIPT_ADDRESS_BYTE_PREFIX
            else:
                prefix = MAINNET_SCRIPT_ADDRESS_LEGACY_BYTE_PREFIX
        address_hash = prefix + address_hash
        address_hash += double_sha256(address_hash)[:4]
        return encode_base58(address_hash)

    if testnet:
        prefix = TESTNET_SEGWIT_ADDRESS_BYTE_PREFIX
        hrp = TESTNET_SEGWIT_ADDRESS_PREFIX
    else:
        prefix = MAINNET_SEGWIT_ADDRESS_BYTE_PREFIX
        hrp = MAINNET_SEGWIT_ADDRESS_PREFIX

    address_hash = b"%s%s" % (witness_version.to_bytes(1, "big"),
                              rebase_8_to_5(address_hash))
    checksum = bech32_polymod(b"%s%s%s" % (prefix, address_hash, b"\x00" * 6))
    checksum = rebase_8_to_5(checksum.to_bytes(5, "big"))[2:]
    return "%s1%s" % (hrp, rebase_5_to_32(address_hash + checksum).decode())

def public_key_to_address(pubkey, testnet=False, p2sh_p2wpkh=False, witness_version=0):
    """
    Get address from public key/script hash. In case PUBKEY, P2PKH, P2PKH public key/script hash is SHA256+RIPEMD160,
    P2WSH script hash is SHA256.
    :param pubkey: public key HEX or bytes string format.
    :param testnet: (optional) flag for testnet network, by default is False.
    :param p2sh_p2wpkh: (optional) flag for P2WPKH inside P2SH address, by default is False.
    :param witness_version: (optional) witness program version, by default is 0, for legacy
                            address format use None.
    :return: address in base58 or bech32 format.
    """
    return __parent__.public_key_to_address(pubkey, testnet=testnet,
                                        p2sh_p2wpkh=p2sh_p2wpkh, witness_version=witness_version)

def address_to_hash(address, hex=True):
    """
    Get address hash from base58 or bech32 address format.
    :param address: address in base58 or bech32 format.
    :param hex:  (optional) If set to True return key in HEX format, by default is True.
    :return: script in HEX or bytes string.
    """
    return __parent__.address_to_hash(address, hex=hex)


def address_type(address, num=False):
    """
    Get address type.
    :param address: address in base58 or bech32 format.
    :param num: (optional) If set to True return type in numeric format, by default is False.
    :return: address type in string or numeric format.
    """
    if address[0] in (TESTNET_SCRIPT_ADDRESS_PREFIX,
                      TESTNET_SCRIPT_ADDRESS_LEGACY_PREFIX,
                      MAINNET_SCRIPT_ADDRESS_PREFIX,
                      MAINNET_SCRIPT_ADDRESS_LEGACY_PREFIX):
        t = 'P2SH'
    elif address[0] in (MAINNET_ADDRESS_PREFIX,
                        TESTNET_ADDRESS_PREFIX,
                        TESTNET_ADDRESS_PREFIX_2):
        t = 'P2PKH'
    elif address.split('1')[0] in (MAINNET_SEGWIT_ADDRESS_PREFIX,
                                   TESTNET_SEGWIT_ADDRESS_PREFIX):
        if len(address) in (43, 44):
            t = 'P2WPKH'
        elif len(address) in (64, 63):
            t = 'P2WSH'
        else:
            return SCRIPT_TYPES['NON_STANDARD'] if num else 'UNKNOWN'
    else:
        return SCRIPT_TYPES['NON_STANDARD'] if num else 'UNKNOWN'
    return SCRIPT_TYPES[t] if num else t

def address_net_type(address):
    """
    Get address network type.
    :param address: address in base58 or bech32 format.
    :return: address network type in string format or None.
    """
    if address[0] in (MAINNET_SCRIPT_ADDRESS_PREFIX,
                      MAINNET_SCRIPT_ADDRESS_LEGACY_PREFIX,
                      MAINNET_ADDRESS_PREFIX):
        return "mainnet"
    elif address[:3] == MAINNET_SEGWIT_ADDRESS_PREFIX:
        return "mainnet"
    elif address[0] in (TESTNET_SCRIPT_ADDRESS_PREFIX,
                        TESTNET_SCRIPT_ADDRESS_LEGACY_PREFIX,
                        TESTNET_ADDRESS_PREFIX,
                        TESTNET_ADDRESS_PREFIX_2):
        return "testnet"
    elif address[:4] == TESTNET_SEGWIT_ADDRESS_PREFIX:
        return "testnet"
    return None

def address_to_script(address, hex=False):
    """
    Get public key script from address.
    :param address: address in base58 or bech32 format.
    :param hex:  (optional) If set to True return key in HEX format, by default is True.
    :return: public key script in HEX or bytes string.
    """
    if address[0] in (TESTNET_SCRIPT_ADDRESS_PREFIX,
                      TESTNET_SCRIPT_ADDRESS_LEGACY_PREFIX,
                      MAINNET_SCRIPT_ADDRESS_PREFIX,
                      MAINNET_SCRIPT_ADDRESS_LEGACY_PREFIX):
        s = [OP_HASH160,
             b'\x14',
             address_to_hash(address, hex=False),
             OP_EQUAL]
    elif address[0] in (MAINNET_ADDRESS_PREFIX,
                        TESTNET_ADDRESS_PREFIX,
                        TESTNET_ADDRESS_PREFIX_2):
        s = [OP_DUP,
             OP_HASH160,
             b'\x14',
             address_to_hash(address, hex=False),
             OP_EQUALVERIFY,
             OP_CHECKSIG]
    elif address.split('1')[0] in (TESTNET_SEGWIT_ADDRESS_PREFIX,
                         MAINNET_SEGWIT_ADDRESS_PREFIX):
        h = address_to_hash(address, hex=False)
        s = [OP_0,
             bytes([len(h)]),
             h]
    else:
        raise ValueError("address invalid")
    s = b''.join(s)
    return s.hex() if hex else s


def public_key_to_p2sh_p2wpkh_script(pubkey):
    return __parent__.public_key_to_p2sh_p2wpkh_script(pubkey)



def is_address_valid(address, testnet=False):
    """
    Check is address valid.
    :param address: address in base58 or bech32 format.
    :param testnet: (optional) flag for testnet network, by default is False.
    :return: boolean.
    """
    if not address or type(address) != str:
        return False
    if address[0] in (MAINNET_ADDRESS_PREFIX,
                      MAINNET_SCRIPT_ADDRESS_PREFIX,
                      MAINNET_SCRIPT_ADDRESS_LEGACY_PREFIX,
                      TESTNET_ADDRESS_PREFIX,
                      TESTNET_ADDRESS_PREFIX_2,
                      TESTNET_SCRIPT_ADDRESS_PREFIX,
                      TESTNET_SCRIPT_ADDRESS_LEGACY_PREFIX):
        if testnet:
            if address[0] not in (TESTNET_ADDRESS_PREFIX,
                                  TESTNET_ADDRESS_PREFIX_2,
                                  TESTNET_SCRIPT_ADDRESS_PREFIX,
                                  TESTNET_SCRIPT_ADDRESS_LEGACY_PREFIX):
                return False
        else:
            if address[0] not in (MAINNET_ADDRESS_PREFIX,
                                  MAINNET_SCRIPT_ADDRESS_PREFIX,
                                  MAINNET_SCRIPT_ADDRESS_LEGACY_PREFIX):
                return False
        h = decode_base58(address)
        if len(h) != 25:
            return False
        checksum = h[-4:]
        if double_sha256(h[:-4])[:4] != checksum:
            return False
        return True
    elif address.split('1')[0].lower() in (TESTNET_SEGWIT_ADDRESS_PREFIX,
                                           MAINNET_SEGWIT_ADDRESS_PREFIX):
        if len(address) not in (43,44, 63, 64):
            return False
        try:
            prefix, payload = address.split('1')
        except:
            return False
        upp = True if prefix[0].isupper() else False
        for i in payload[1:]:
            if upp:
                if not i.isupper() or i not in base32charset_upcase:
                    return False
            else:
                if i.isupper() or i not in base32charset:
                    return False
        payload = payload.lower()
        prefix = prefix.lower()
        if testnet:
            if prefix != TESTNET_SEGWIT_ADDRESS_PREFIX:
                return False
            stripped_prefix = TESTNET_SEGWIT_ADDRESS_BYTE_PREFIX
        else:
            if prefix != MAINNET_SEGWIT_ADDRESS_PREFIX:
                return False
            stripped_prefix = MAINNET_SEGWIT_ADDRESS_BYTE_PREFIX
        d = rebase_32_to_5(payload)
        address_hash = d[:-6]
        checksum = d[-6:]
        checksum2 = bech32_polymod(stripped_prefix + address_hash + b"\x00" * 6)
        checksum2 = rebase_8_to_5(checksum2.to_bytes(5, "big"))[2:]
        if checksum != checksum2:
            return False
        return True
    return False


def get_witness_version(address):
    return __parent__.get_witness_version(address)
