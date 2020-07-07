import pybtc.functions.script as __parent__
from pyltc.constants import  *

from pyltc.functions.address import hash_to_address

def public_key_to_pubkey_script(key, hex=True):
    return __parent__.public_key_to_pubkey_script(key, hex=hex)


def parse_script(script, segwit=True):
    """
    Parse script and return script type, script address and required signatures count.

    :param script: script in bytes string or HEX encoded string format.
    :param segwit:  (optional) If set to True recognize P2WPKH and P2WSH sripts, by default set to True.

    :return: dictionary:

            - nType - numeric script type
            - type  - script type
            - addressHash - address hash in case address recognized
            - script - script if no address recognized
            - reqSigs - required signatures count
    """
    return  __parent__.parse_script(script, segwit=segwit)


def script_to_address(script, testnet=False, legacy=False):
    """
    Decode script to address (base58/bech32 format).

    :param script: script in bytes string or HEX encoded string format.
    :param testnet: (optional) flag for testnet network, by default is False.
    :return: address in base58/bech32 format or None.
    """
    d = parse_script(script)
    if "addressHash" in d:
        witness_version = 0 if d["nType"] in (5, 6) else None
        script_hash = True if d["nType"] in (1, 6) else False
        return hash_to_address(d["addressHash"], testnet=testnet,
                               script_hash=script_hash, witness_version=witness_version, legacy=legacy)
    return None


def decode_script(script, asm=False):
    """
    Decode script to ASM format or to human readable OPCODES string.

    :param script: script in bytes string or HEX encoded string format.
    :param asm:  (optional) If set to True decode to ASM format, by default set to False.
    :return: script in ASM format string or OPCODES string.
    """

    return __parent__.decode_script(script, asm=asm)


def delete_from_script(script, sub_script):
    """
    Decode OP_CODE or subscript from script.

    :param script: target script in bytes or HEX encoded string.
    :param sub_script:  sub_script which is necessary to remove from target script in bytes or HEX encoded string.
    :return: script in bytes or HEX encoded string corresponding to the format of target script.
    """
    return __parent__.delete_from_script(script, sub_script)


def script_to_hash(script, witness=False, hex=True):
    """
    Encode script to hash HASH160 or SHA256 in dependency of the witness.

    :param script: script in bytes or HEX encoded string.
    :param witness:  (optional) If set to True return SHA256 hash for P2WSH, by default is False.
    :param hex:  (optional) If set to True return key in HEX format, by default is True.
    :param sub_script:  sub_script which is necessary to remove from target script in bytes or HEX encoded string.
    :return: script in bytes or HEX encoded string corresponding to the format of target script.
    """
    return __parent__.script_to_hash(script, witness=witness, hex=hex)


def op_push_data(data):
    return __parent__.op_push_data(data)


def get_multisig_public_keys(script):
    return __parent__.get_multisig_public_keys(script)


def read_opcode(stream):
    return __parent__.read_opcode(stream)


def verify_signature(sig, pub_key, msg):
    return __parent__.verify_signature(sig, pub_key, msg)


def sign_message(msg, private_key, hex=True):
    return __parent__.sign_message(msg, private_key, hex=hex)


def public_key_recovery(signature, messsage, rec_id, compressed=True, hex=True):
    return __parent__.public_key_recovery(signature, messsage, rec_id, compressed=compressed, hex=hex)


def is_valid_signature_encoding(sig):
    return __parent__.is_valid_signature_encoding(sig)