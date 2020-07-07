import pybtc.functions.bip39_mnemonic as __parent__


def generate_entropy(strength=256, hex=True):
    """
    Generate 128-256 bits entropy bytes string

    :param int strength: entropy bits strength, by default is 256 bit.
    :param boolean hex: return HEX encoded string result flag, by default True.
    :return: HEX encoded or bytes entropy string.
    """
    return __parent__.generate_entropy(strength=strength, hex=hex)


def load_word_list(language='english', word_list_dir=None):
    """
    Load the word list from local file.

    :param str language: (optional) uses word list language (chinese_simplified, chinese_traditional, english, french,
                         italian, japanese, korean, spanish), by default is english.
    :param str word_list_dir: (optional) path to a directory containing a list of words,
                              by default None (use BIP39 standard list)
    :return: list of words.
    """
    return __parent__.load_word_list(language=language, word_list_dir=word_list_dir)


def entropy_to_mnemonic(entropy, language='english', word_list_dir=None, word_list=None):
    """
    Convert entropy to mnemonic words string.

    :param str,bytes entropy: random entropy HEX encoded or bytes string.
    :param str language: (optional) uses word list language (chinese_simplified, chinese_traditional, english, french,
                         italian, japanese, korean, spanish), by default is english.
    :param str word_list_dir: (optional) path to a directory containing a list of words,
                              by default None (use BIP39 standard list)
    :param list word_list: (optional) already loaded word list, by default None
    :return: mnemonic words string.
    """
    return __parent__.entropy_to_mnemonic(entropy, language=language, word_list_dir=word_list_dir, word_list=word_list)


def mnemonic_to_entropy(mnemonic, language='english', word_list_dir=None,
                        word_list=None, hex=True):
    """
    Converting mnemonic words to entropy.

    :param str mnemonic: mnemonic words string (space separated)
    :param str language: (optional) uses word list language (chinese_simplified, chinese_traditional, english, french,
                         italian, japanese, korean, spanish), by default is english.
    :param str word_list_dir: (optional) path to a directory containing a list of words,
                              by default None (use BIP39 standard list)
    :param list word_list: (optional) already loaded word list, by default None
    :param boolean hex: return HEX encoded string result flag, by default True.
    :return: bytes string.
    """
    return __parent__.mnemonic_to_entropy(mnemonic, language=language, word_list_dir=word_list_dir,
                                      word_list=word_list, hex=hex)


def mnemonic_to_seed(mnemonic, passphrase="", hex=True):
    """
    Converting mnemonic words string to seed for uses in key derivation (BIP-0032).

    :param str mnemonic: mnemonic words string (space separated)
    :param str passphrase: (optional) passphrase to get ability use 2FA approach for
                          creating seed, by default empty string.
    :param boolean hex: return HEX encoded string result flag, by default True.
    :return: HEX encoded or bytes string.
    """
    return __parent__.mnemonic_to_seed(mnemonic, passphrase=passphrase, hex=hex)
