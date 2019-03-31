
import _scrypt

def get_scrypt_hash(header, hex=False):
    if isinstance(header, str):
        header = bytes.fromhex(header)
    if not isinstance(header, bytes):
        raise TypeError("block header should be bytes or hex encoded string")
    if hex:
        return _scrypt.getScryptHash(header).hex()
    else:
        return _scrypt.getScryptHash(header)