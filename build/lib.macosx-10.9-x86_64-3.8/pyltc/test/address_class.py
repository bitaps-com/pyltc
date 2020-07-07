import unittest
import os
import sys


parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)

# from pyltc.transaction import *
from pyltc import OPCODE
from binascii import unhexlify
import pyltc

class AddressClassTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nTesting address class:\n")

    def test_is_WIF_valid(self):
        # mainnet
        self.assertEqual(pyltc.PrivateKey("7fbda89e59e07db5897cabfde8eb8036d4bebdfddfeac97319e74c74c02799f2",
                                            compressed=True, testnet=False).wif,
                         'T7LHhPHG4mno7XPvBXajDrA5v2nLVSw16sTErD9y6Yki3bGTuHgf')
        self.assertEqual(pyltc.PrivateKey("aaf19a8a8eacca26b2ec3678e47ee22a04fc1efac61bcd2a41af332be63bab8b",
                                            compressed=False, testnet=False).wif,
                         '6vRJaVegzBxTXdgGEimmmSsEv1CLdAgfpaHsZbXUxkPfm9H8U7X')
        # # testnet
        self.assertEqual(pyltc.PrivateKey("fef231a9299de5b2d3ea012cd2471bdc80d38e489f5f4a7803ac3279a7d727a9",
                                            compressed=True, testnet=True).wif,
                         'cW8HPuCThQ4EsLEU8S6Gborp7NfwXDc2uh2Aua83kmhjqN8GzEVk')
        self.assertEqual(pyltc.PrivateKey("fc1528167b31735464059aef58cf71b501eaa146bae7e47f406c61f7ac28555c",
                                            compressed=False, testnet=True).wif,
                         '93VwGxfztHBcUefSWA3JMzKsr6Jg4atmZdKvi1MXTgB9HLypXry')

        self.assertEqual(pyltc.PrivateKey("cW8HPuCThQ4EsLEU8S6Gborp7NfwXDc2uh2Aua83kmhjqN8GzEVk",
                                            compressed=False, testnet=True).wif,
                         'cW8HPuCThQ4EsLEU8S6Gborp7NfwXDc2uh2Aua83kmhjqN8GzEVk')

        p = pyltc.PrivateKey("7b56e2b7bd189f4491d43a1d209e6268046df1741f61b6397349d7aa54978e76")
        pub = pyltc.PublicKey(p)
        a = pyltc.Address(p)
        # self.assertEqual(a.address, 'bc1qxsms4rt5axt9674du2az7vq3pvephu3k5jyky8')
        # a = pyltc.Address(p, address_type = "P2PKH")
        # self.assertEqual(a.address, '15m65JmFohJiioQbzMWhqFeCS3ZL1KVaNh')
        # a = pyltc.Address(p, address_type = "PUBKEY")
        # self.assertEqual(a.address, '15m65JmFohJiioQbzMWhqFeCS3ZL1KVaNh')
        a = pyltc.Address(p, address_type = "P2SH_P2WPKH", legacy=True)
        self.assertEqual(a.address, '37WJdFAoHDbxUQioDgtvPZuyJPyrrNQ7aL')
        self.assertEqual(a.redeem_script_hex, '001434370a8d74e9965d7aade2ba2f30110b321bf236')
        self.assertEqual(a.public_key.hex, '02a8fb85e98c99b79150df12fde488639d8445c57babef83d53c66c1e5c818eeb4')
        #
        cpk = "02a8fb85e98c99b79150df12fde488639d8445c57babef83d53c66c1e5c818eeb4"
        ucpk = "04a8fb85e98c99b79150df12fde488639d8445c57babef83d53c66c1e5c818eeb" \
               "43bbd96a641808e5f34eb568e804fe679de82de419e2512736ea09013a82324a6"
        # public key uncompressed from HEX private
        self.assertEqual(pyltc.PublicKey("7b56e2b7bd189f4491d43a1d209e6268046df1741f61b6397349d7aa54978e76",
                                           compressed=False).hex, ucpk)
        # public key compressed from HEX private
        self.assertEqual(pyltc.PublicKey("7b56e2b7bd189f4491d43a1d209e6268046df1741f61b6397349d7aa54978e76",
                                           compressed=True).hex, cpk)
        # # public key compressed from WIF private
        # self.assertEqual(pyltc.PublicKey("L1MU1jUjUwZ6Fd1L2HDZ8qH4oSWxct5boCQ4C87YvoSZbTW41hg4",
        #                                    compressed=False).hex, cpk)
        # # public key compressed from  PrivateKey instance (flags have no effect)
        # p = pyltc.PrivateKey("L1MU1jUjUwZ6Fd1L2HDZ8qH4oSWxct5boCQ4C87YvoSZbTW41hg4")
        # self.assertEqual(pyltc.PublicKey(p, compressed=False).hex, cpk)
        #
        # # public key compressed from  public
        # self.assertEqual(pyltc.PublicKey(cpk, compressed=False).hex, cpk)
        #
        # # public key compressed from  public
        # self.assertEqual(pyltc.PublicKey(unhexlify(cpk), compressed=False).hex, cpk)
        #
        # # compressed public key
        # # private key hex string to compressed pub key
        # p = pyltc.PrivateKey("7b56e2b7bd189f4491d43a1d209e6268046df1741f61b6397349d7aa54978e76", compressed=False)
        # pub = pyltc.PublicKey(p)
        # a = pyltc.Address(p, address_type="P2PKH")
        # self.assertEqual(a.address, '17suVjHXyWF9KiGkpRRQW4ysiEqdDkRqo1')
        # a = pyltc.Address(p, address_type="PUBKEY")
        # self.assertEqual(a.address, '17suVjHXyWF9KiGkpRRQW4ysiEqdDkRqo1')
        #
        # from pubkey
        p = pyltc.PublicKey('02a8fb85e98c99b79150df12fde488639d8445c57babef83d53c66c1e5c818eeb4')
        a = pyltc.Address(p)
        # self.assertEqual(a.address, 'bc1qxsms4rt5axt9674du2az7vq3pvephu3k5jyky8')
        # a = pyltc.Address(p, address_type="P2PKH")
        # self.assertEqual(a.address, '15m65JmFohJiioQbzMWhqFeCS3ZL1KVaNh')
        # a = pyltc.Address(p, address_type="PUBKEY")
        # self.assertEqual(a.address, '15m65JmFohJiioQbzMWhqFeCS3ZL1KVaNh')
        a = pyltc.Address(p, address_type="P2SH_P2WPKH", legacy=True)
        self.assertEqual(a.address, '37WJdFAoHDbxUQioDgtvPZuyJPyrrNQ7aL')
        self.assertEqual(a.redeem_script_hex, '001434370a8d74e9965d7aade2ba2f30110b321bf236')
        self.assertEqual(a.public_key.hex, '02a8fb85e98c99b79150df12fde488639d8445c57babef83d53c66c1e5c818eeb4')
        #
        # # from uncompressed pubkey
        p = pyltc.PublicKey('04a8fb85e98c99b79150df12fde488639d8445c57babef83d53c66c1e5c818eeb43bbd96a641808'
                              'e5f34eb568e804fe679de82de419e2512736ea09013a82324a6')
        # a = pyltc.Address(p, address_type="P2PKH")
        # self.assertEqual(a.address, '17suVjHXyWF9KiGkpRRQW4ysiEqdDkRqo1')
        # a = pyltc.Address(p, address_type="PUBKEY")
        # self.assertEqual(a.address, '17suVjHXyWF9KiGkpRRQW4ysiEqdDkRqo1')
        #
        redeem = "5221032bfc25cf7cccc278b26473e2967b8fd403b4b544b836e71abdfebb08d8c96d6921032bfc25cf7cccc278b2" \
                 "6473e2967b8fd403b4b544b836e71abdfebb08d8c96d6921032bfc25cf7cccc278b26473e2967b8fd403b4b544b8" \
                 "36e71abdfebb08d8c96d6953ae"
        a = pyltc.ScriptAddress(redeem, witness_version=None, legacy=True)
        self.assertEqual(a.address, '3KCqqS6eznp3ucVPxtNkiYcVg6kQKNX9sg')



