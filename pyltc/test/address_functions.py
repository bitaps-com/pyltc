import unittest
import os, sys
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)

from pyltc.functions import script as tools
from pyltc import functions
from pyltc import BYTE_OPCODE, HEX_OPCODE
from binascii import unhexlify, hexlify


class AddressFunctionsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nTesting address functions:\n")

    def test_private_key_to_WIF(self):
        p = "aaf19a8a8eacca26b2ec3678e47ee22a04fc1efac61bcd2a41af332be63bab8b"
        wif = "6vRJaVegzBxTXdgGEimmmSsEv1CLdAgfpaHsZbXUxkPfm9H8U7X"
        self.assertEqual(functions.private_key_to_wif(p, compressed=0, testnet=0), wif)

        p = "7fbda89e59e07db5897cabfde8eb8036d4bebdfddfeac97319e74c74c02799f2"
        wif = "T7LHhPHG4mno7XPvBXajDrA5v2nLVSw16sTErD9y6Yki3bGTuHgf"
        self.assertEqual(functions.private_key_to_wif(p, compressed=1, testnet=0), wif)

        p = "fc1528167b31735464059aef58cf71b501eaa146bae7e47f406c61f7ac28555c"
        wif = "93VwGxfztHBcUefSWA3JMzKsr6Jg4atmZdKvi1MXTgB9HLypXry"
        self.assertEqual(functions.private_key_to_wif(p, compressed=0, testnet=1), wif)

        p = "fef231a9299de5b2d3ea012cd2471bdc80d38e489f5f4a7803ac3279a7d727a9"
        wif = "cW8HPuCThQ4EsLEU8S6Gborp7NfwXDc2uh2Aua83kmhjqN8GzEVk"
        self.assertEqual(functions.private_key_to_wif(p, compressed=1, testnet=1), wif)


    #
    # def test_is_WIF_valid(self):
    #     self.assertEqual(functions.is_wif_valid("6vRJaVegzBxTXdgGEimmmSsEv1CLdAgfpaHsZbXUxkPfm9H8U7X"), 1)
    #     self.assertEqual(functions.is_wif_valid("T7LHhPHG4mno7XPvBXajDrA5v2nLVSw16sTErD9y6Yki3bGTuHgf"), 1)
    #     self.assertEqual(functions.is_wif_valid("T7LHh1HG4mno7XPvBXajDrA5v2nLVSw16sTErD9y6Yki3bGTuHgf"), 0)
    #     self.assertEqual(functions.is_wif_valid("93VwGxfztHBcUefSWA3JMzKsr6Jg4atmZdKvi1MXTgB9HLypXry"), 1)
    #     self.assertEqual(functions.is_wif_valid("cW8HPuCThQ4EsLEU8S6Gborp7NfwXDc2uh2Aua83kmhjqN8GzEVk"), 1)
    #     self.assertEqual(functions.is_wif_valid("cW8HPwCThQ4EsLEU8S6Gborp7NfwXDc2uh2Aua83kmhjqN8GzEVk"), 0)
    #
    # def test_WIF_to_private_key(self):
    #     p = "aaf19a8a8eacca26b2ec3678e47ee22a04fc1efac61bcd2a41af332be63bab8b"
    #     wif = "6vRJaVegzBxTXdgGEimmmSsEv1CLdAgfpaHsZbXUxkPfm9H8U7X"
    #     self.assertEqual(functions.wif_to_private_key(wif, hex=1),p)
    #
    #     p = "7fbda89e59e07db5897cabfde8eb8036d4bebdfddfeac97319e74c74c02799f2"
    #     wif = "T7LHhPHG4mno7XPvBXajDrA5v2nLVSw16sTErD9y6Yki3bGTuHgf"
    #     self.assertEqual(functions.wif_to_private_key(wif, hex=1),p)
    #
    #     p = "fc1528167b31735464059aef58cf71b501eaa146bae7e47f406c61f7ac28555c"
    #     wif = "93VwGxfztHBcUefSWA3JMzKsr6Jg4atmZdKvi1MXTgB9HLypXry"
    #     self.assertEqual(functions.wif_to_private_key(wif, hex=1),p)
    #
    #     p = "fef231a9299de5b2d3ea012cd2471bdc80d38e489f5f4a7803ac3279a7d727a9"
    #     wif = "cW8HPuCThQ4EsLEU8S6Gborp7NfwXDc2uh2Aua83kmhjqN8GzEVk"
    #     self.assertEqual(functions.wif_to_private_key(wif, hex=1),p)
    #
    #
    #
    # def test_create_private_key(self):
    #     p = functions.create_private_key(wif=0)
    #     pw = functions.private_key_to_wif(p)
    #     self.assertEqual(functions.is_wif_valid(pw), True)
    #
    #
    #
    # def test_private_to_public_key(self):
    #     p = "ceda1ae4286015d45ec5147fe3f63e9377ccd6d4e98bcf0847df9937da1944a4"
    #     pu = "04b635dbdc16dbdf4bb9cf5b55e7d03e514fb04dcef34208155c7d3ec88e9045f4c8cbe28702911260f2a1da099a338bed4ee98f66bb8dba8031a76ab537ff6663"
    #     pk = "03b635dbdc16dbdf4bb9cf5b55e7d03e514fb04dcef34208155c7d3ec88e9045f4"
    #     self.assertEqual(functions.private_to_public_key(p, hex=1), pk)
    #     self.assertEqual(functions.private_to_public_key(p, hex=0), unhexlify(pk))
    #     self.assertEqual(functions.private_to_public_key(p, compressed=0, hex=1), pu)
    #
    #     self.assertEqual(functions.private_to_public_key("T9z52wpfX3FaoP4rsqPAu16ZVcuxFgLHGKryWW7C7VCbaN2pA6Tt", hex=1), pk)
    #     self.assertEqual(functions.private_to_public_key("6vh7ofFRazc2KDFUAFb2LV7hSWtRJNbjCdSphDV8xPhh1PrWTYt", hex=1), pu)
    #     self.assertEqual(functions.private_to_public_key("93A1vGXSGoDHotruGmgyRgtV8hgfFjgtmtuc4epcag886W9d44L", hex=1), pu)
    #     self.assertEqual(functions.private_to_public_key("cUWo47XLYiyFByuFicFS3y4FAza3r3R5XA7Bm7wA3dgSKDYox7h6", hex=1), pk)
    #
    # def test_hash_to_address(self):
    #     # p2wpkh
    #     h = "751e76e8199196d454941c45d1b3a323f1433bd6"
    #     self.assertEqual(functions.hash_to_address(h), "ltc1qw508d6qejxtdg4y5r3zarvary0c5xw7kgmn4n9")
    #     # p2wsh
    #     h = "1863143c14c5166804bd19203356da136c985678cd4d27a1b8c6329604903262"
    #     self.assertEqual(functions.hash_to_address(h, testnet=1),
    #                      "tltc1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qsnr4fp")
    #     # p2sh
    #     h = "014f2e7072e9907c7f636d937759b8ceb1053feb"
    #     self.assertEqual(functions.hash_to_address(h, testnet=0, witness_version=None, script_hash=True),
    #                      "M825mF1bLC3hPL6ZmaEVqZ2pouU5iRE72D")
    #


        # s =  bytes([len(unhexlify(pc))])+unhexlify(pc) + BYTE_OPCODE["OP_CHECKSIG"]
        # self.assertEqual(functions.hash_to_address(h, testnet=1), "tb1qw508d6qejxtdg4y5r3zarvary0c5xw7kxpjzsx")
        # h = tools.script_to_hash(s, 1, 1)
        # self.assertEqual(functions.hash_to_address(h), "bc1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qccfmv3")
        # self.assertEqual(functions.hash_to_address(h, testnet=1), "tb1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3q0sl5k7")
        # pk = "03b635dbdc16dbdf4bb9cf5b55e7d03e514fb04dcef34208155c7d3ec88e9045f4"
        # h = tools.hash160(pk)
        # self.assertEqual(functions.hash_to_address(h, witness_version=None), "1Fs2Xqrk4P2XADaJeZWykaGXJ4HEb6RyT1")
        # self.assertEqual(functions.hash_to_address(h, witness_version=None, testnet=1),
        #                  "mvNyptwisQTmwL3vN8VMaVUrA3swVCX83c")
        # # p2wpkh inside p2sh
        # p = "L32a8Mo1LgvjrVDbzcc3NkuUfkpoLsf2Y2oEWkV4t1KpQdFzuyff"
        # pk = functions.private_to_public_key(p)
        # script = b'\x00\x14' + tools.hash160(pk)
        # script_hash = tools.hash160(script)
        # self.assertEqual(functions.hash_to_address(script_hash,
        #                                            script_hash=1,
        #                                            witness_version=None), "33am12q3Bncnn3BfvLYHczyv23Sq2Wbwjw")
        # self.assertEqual(functions.hash_to_address(script_hash,
        #                                            script_hash=1,
        #                                            witness_version=None,
        #                                            testnet=1), "2Mu8y4mm4oF88yppDbUAAEwyBEPezrx7CLh")
    #
    # def test_address_to_hash(self):
    #     h = "751e76e8199196d454941c45d1b3a323f1433bd6"
    #     self.assertEqual(functions.address_to_hash("bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4", 1), h)
    #     self.assertEqual(functions.address_to_hash("tb1qw508d6qejxtdg4y5r3zarvary0c5xw7kxpjzsx", 1), h)
    #     h  = "1863143c14c5166804bd19203356da136c985678cd4d27a1b8c6329604903262"
    #     self.assertEqual(functions.address_to_hash("bc1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qccfmv3", 1), h)
    #     h = "a307d67484911deee457779b17505cedd20e1fe9"
    #     self.assertEqual(functions.address_to_hash("1Fs2Xqrk4P2XADaJeZWykaGXJ4HEb6RyT1", 1), h)
    #     self.assertEqual(functions.address_to_hash("mvNyptwisQTmwL3vN8VMaVUrA3swVCX83c", 1), h)
    #     h = "14c14c8d26acbea970757b78e6429ad05a6ac6bb"
    #     self.assertEqual(functions.address_to_hash("33am12q3Bncnn3BfvLYHczyv23Sq2Wbwjw", 1), h)
    #     self.assertEqual(functions.address_to_hash("2Mu8y4mm4oF88yppDbUAAEwyBEPezrx7CLh", 1), h)
    #
    # def test_address_type(self):
    #     self.assertEqual(functions.address_type("bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4"), 'P2WPKH')
    #     self.assertEqual(functions.address_type("tb1qw508d6qejxtdg4y5r3zarvary0c5xw7kxpjzsx"), 'P2WPKH')
    #     self.assertEqual(functions.address_type("bc1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qccfmv3"), 'P2WSH')
    #     self.assertEqual(functions.address_type("tb1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3q0sl5k7"), 'P2WSH')
    #     self.assertEqual(functions.address_type("1Fs2Xqrk4P2XADaJeZWykaGXJ4HEb6RyT1"), 'P2PKH')
    #     self.assertEqual(functions.address_type("mvNyptwisQTmwL3vN8VMaVUrA3swVCX83c"), 'P2PKH')
    #     self.assertEqual(functions.address_type("33am12q3Bncnn3BfvLYHczyv23Sq2Wbwjw"), 'P2SH')
    #     self.assertEqual(functions.address_type("2Mu8y4mm4oF88yppDbUAAEwyBEPezrx7CLh"), 'P2SH')
    #
    # def test_address_net_type(self):
    #     self.assertEqual(functions.address_net_type("bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4"), 'mainnet')
    #     self.assertEqual(functions.address_net_type("tb1qw508d6qejxtdg4y5r3zarvary0c5xw7kxpjzsx"), 'testnet')
    #     self.assertEqual(functions.address_net_type("bc1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qccfmv3"),
    #                      'mainnet')
    #     self.assertEqual(functions.address_net_type("tb1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3q0sl5k7"),
    #                      'testnet')
    #     self.assertEqual(functions.address_net_type("1Fs2Xqrk4P2XADaJeZWykaGXJ4HEb6RyT1"), 'mainnet')
    #     self.assertEqual(functions.address_net_type("mvNyptwisQTmwL3vN8VMaVUrA3swVCX83c"), 'testnet')
    #     self.assertEqual(functions.address_net_type("33am12q3Bncnn3BfvLYHczyv23Sq2Wbwjw"), 'mainnet')
    #     self.assertEqual(functions.address_net_type("2Mu8y4mm4oF88yppDbUAAEwyBEPezrx7CLh"), 'testnet')
    #
    # def test_public_key_to_address(self):
    #     pc = "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798"
    #     self.assertEqual(functions.public_key_to_address(pc), "bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4")
    #     self.assertEqual(functions.public_key_to_address(pc, testnet=1), "tb1qw508d6qejxtdg4y5r3zarvary0c5xw7kxpjzsx")
    #     pc = "03b635dbdc16dbdf4bb9cf5b55e7d03e514fb04dcef34208155c7d3ec88e9045f4"
    #     self.assertEqual(functions.public_key_to_address(pc,
    #                                                  witness_version=None,
    #                                                  testnet=0), "1Fs2Xqrk4P2XADaJeZWykaGXJ4HEb6RyT1")
    #     self.assertEqual(functions.public_key_to_address(pc, witness_version=None,
    #                                                  testnet=1), "mvNyptwisQTmwL3vN8VMaVUrA3swVCX83c")
    #     p = "L32a8Mo1LgvjrVDbzcc3NkuUfkpoLsf2Y2oEWkV4t1KpQdFzuyff"
    #     pk = functions.private_to_public_key(p)
    #     self.assertEqual(functions.public_key_to_address(pk, p2sh_p2wpkh=1,
    #                                                  witness_version=None), "33am12q3Bncnn3BfvLYHczyv23Sq2Wbwjw")
    #
    # def test_is_address_valid(self):
    #     self.assertEqual(functions.is_address_valid("bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4"), 1)
    #     self.assertEqual(functions.is_address_valid("tb1qw508d6qejxtdg4y5r3zarvary0c5xw7kxpjzsx", 1), 1)
    #     self.assertEqual(functions.is_address_valid("tb1qw508d6qejxtdg4y5r3zarvary0c5xw7kxpjzsx"), 0)
    #     self.assertEqual(functions.is_address_valid("bc1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qccfmv3"), 1)
    #     self.assertEqual(functions.is_address_valid("tb1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3q0sl5k7", 1), 1)
    #     self.assertEqual(functions.is_address_valid("1Fs2Xqrk4P2XADaJeZWykaGXJ4HEb6RyT1"), 1)
    #     self.assertEqual(functions.is_address_valid("mvNyptwisQTmwL3vN8VMaVUrA3swVCX83c", 1), 1)
    #     self.assertEqual(functions.is_address_valid("33am12q3Bncnn3BfvLYHczyv23Sq2Wbwjw"), 1)
    #     self.assertEqual(functions.is_address_valid("2Mu8y4mm4oF88yppDbUAAEwyBEPezrx7CLh",1), 1)
    #     self.assertEqual(functions.is_address_valid("2Mu8y4mm4oF89yppDbUAAEwyBEPezrx7CLh",1), 0)
    #     self.assertEqual(functions.is_address_valid("bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4", 1), 0)
    #     self.assertEqual(functions.is_address_valid("tb1qw508d6qejxtdg4W5r3zarvary0c5xw7kxpjzsx",1), 0)
    #     self.assertEqual(functions.is_address_valid("bc1qrp33g0q5c5txsp8arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qccfmv3"), 0)
    #     self.assertEqual(functions.is_address_valid("tb1qrp23g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3q0sl5k7",1), 0)
    #     self.assertEqual(functions.is_address_valid("1Fs2Xqrk4P2XADaJeZWykaGXJ2HEb6RyT1"), 0)
    #     self.assertEqual(functions.is_address_valid("mvNyptwisQTkwL3vN8VMaVUrA3swVCX83c", 1), 0)
    #     self.assertEqual(functions.is_address_valid("33am12q3Bncmn3BfvLYHczyv23Sq2Wbwjw"), 0)
    #     self.assertEqual(functions.is_address_valid("2Mu8y4mm4oF78yppDbUAAEwyBEPezrx7CLh", 1), 0)
    #
    # def test_address_to_script(self):
    #     self.assertEqual(functions.address_to_script("17rPqUf4Hqu6Lvpgfsavt1CzRy2GL19GD3", 1),
    #                      "76a9144b2832feeda5692c96c0594a6314136a998f515788ac")
    #     self.assertEqual(functions.address_to_script("33RYUa9jT541UNPsKdV7V1DmwMiQHpVfD3", 1),
    #                      "a914130319921ecbcfa33fec2a8503c4ae1c86e4419387")
    #     self.assertEqual(functions.address_to_script("bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4", 1),
    #                      "0014751e76e8199196d454941c45d1b3a323f1433bd6")
    #     self.assertEqual(functions.address_to_script("bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4", 1),
    #                      "0014751e76e8199196d454941c45d1b3a323f1433bd6")
    #
    # def test_parse_script(self):
    #
    #     k = tools.parse_script("76a9144b2832feeda5692c96c0594a6314136a998f515788ac")
    #     address = functions.hash_to_address(k["addressHash"], witness_version = None)
    #     self.assertEqual(address, "17rPqUf4Hqu6Lvpgfsavt1CzRy2GL19GD3")
    #     self.assertEqual(k["type"],"P2PKH")
    #     self.assertEqual(k["nType"],0)
    #     self.assertEqual(k["reqSigs"],1)
    #     self.assertEqual(functions.address_to_script(address, 1),
    #                      "76a9144b2832feeda5692c96c0594a6314136a998f515788ac")
    #
    #     k = tools.parse_script("76a914a307d67484911deee457779b17505cedd20e1fe988ac")
    #     address = functions.hash_to_address(k["addressHash"], testnet= True, witness_version=None)
    #     self.assertEqual(address,"mvNyptwisQTmwL3vN8VMaVUrA3swVCX83c")
    #     self.assertEqual(k["type"],"P2PKH")
    #     self.assertEqual(k["nType"],0)
    #     self.assertEqual(k["reqSigs"],1)
    #     self.assertEqual(functions.address_to_script(address, 1),
    #                      "76a914a307d67484911deee457779b17505cedd20e1fe988ac")
    #
    #     k = tools.parse_script("a914b316ac9bdd0816ecdec6773d1192c0eaf52ae66487")
    #     address = functions.hash_to_address(k["addressHash"], script_hash=True, witness_version=None)
    #     self.assertEqual(address, "3J1x3KHjgjoTjqHjrwKax2zeT8LSDkZJae")
    #     self.assertEqual(k["type"],"P2SH")
    #     self.assertEqual(k["nType"],1)
    #     self.assertEqual(k["reqSigs"], None)
    #     self.assertEqual(functions.address_to_script(address, 1),
    #                      "a914b316ac9bdd0816ecdec6773d1192c0eaf52ae66487")
    #
    #     k = tools.parse_script("0014751e76e8199196d454941c45d1b3a323f1433bd6")
    #     address = functions.hash_to_address(k["addressHash"], script_hash=False,
    #                                     witness_version=0, testnet=False)
    #     self.assertEqual(address, "bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4")
    #     self.assertEqual(k["type"],"P2WPKH")
    #     self.assertEqual(k["nType"],5)
    #     self.assertEqual(k["reqSigs"],1)
    #     self.assertEqual(functions.address_to_script(address, 1),
    #                      "0014751e76e8199196d454941c45d1b3a323f1433bd6")
    #
    #     s = [HEX_OPCODE['OP_HASH160'],
    #          '14',
    #          '92c2f2da37093971ca335824edae06468e60ea20',
    #          HEX_OPCODE['OP_EQUAL']]
    #     h = ''.join(s)
    #     s = unhexlify(h)
    #     k = tools.parse_script(s)
    #     address = functions.hash_to_address(k["addressHash"], script_hash=True,
    #                                     witness_version=None, testnet=False)
    #     self.assertEqual(address, "3F527pX8o2pgr6FuNdNvngA2Do2wVvDoZi")
    #     self.assertEqual(k["type"],"P2SH")
    #     self.assertEqual(k["nType"],1)
    #     self.assertEqual(k["reqSigs"], None)
    #     self.assertEqual(functions.address_to_script(address, 1), h)
    #
    #     s = [HEX_OPCODE['OP_3'],
    #          '21',
    #          '021ecd2e5eb5dbd7c8e59f66e37da2ae95f7d61a07f4b2567c3bb10bbb1b2ec953',
    #          '21',
    #          '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
    #          '21',
    #          '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
    #          '21',
    #          '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
    #          '21',
    #          '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
    #          '21',
    #          '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
    #          HEX_OPCODE['OP_6'],
    #          HEX_OPCODE['OP_CHECKMULTISIG']]
    #     h = ''.join(s)
    #     s = unhexlify(h)
    #     k = tools.parse_script(s)
    #     sh = tools.script_to_hash(h, 0, 0)
    #     address = functions.hash_to_address(sh,script_hash=True,
    #                                     witness_version=None, testnet=False)
    #     self.assertEqual(address, "3D2oetdNuZUqQHPJmcMDDHYoqkyNVsFk9r")
    #     self.assertEqual(k["type"],"MULTISIG")
    #     self.assertEqual(k["nType"],4)
    #     self.assertEqual(k["reqSigs"],3)
    #
    #     s = [HEX_OPCODE['OP_0'],
    #          '21',
    #          '021ecd2e5eb5dbd7c8e59f66e37da2ae95f7d61a07f4b2567c3bb10bbb1b2ec953',
    #          '21',
    #          '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
    #          '21',
    #          '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
    #          '21',
    #          '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
    #          '21',
    #          '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
    #          '21',
    #          '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
    #          HEX_OPCODE['OP_6'],
    #          HEX_OPCODE['OP_CHECKMULTISIG']]
    #     h = ''.join(s)
    #     s = unhexlify(h)
    #     k = tools.parse_script(s)
    #     sh = tools.script_to_hash(h, 0,0)
    #     self.assertEqual(k["type"],"NON_STANDARD")
    #     self.assertEqual(k["nType"],7)
    #     self.assertEqual(k["reqSigs"],20)
    #
    #     s = [HEX_OPCODE['OP_1'],
    #          '21',
    #          '021ecd2e5eb5dbd7c8e59f66e37da2ae95f7d61a07f4b2567c3bb10bbb1b2ec953',
    #          '21',
    #          '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
    #          '21',
    #          '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
    #          '21',
    #          '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
    #          '21',
    #          '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
    #          '21',
    #          '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
    #          HEX_OPCODE['OP_6'],
    #          HEX_OPCODE['OP_CHECKMULTISIG']]
    #     h = ''.join(s)
    #     s = unhexlify(h)
    #     k = tools.parse_script(s)
    #     self.assertEqual(k["type"],"MULTISIG")
    #     self.assertEqual(k["nType"],4)
    #     self.assertEqual(k["reqSigs"],1)
    #
    #
    #
    #     s = [HEX_OPCODE['OP_1'],
    #          HEX_OPCODE['OP_1'],
    #          '21',
    #          '021ecd2e5eb5dbd7c8e59f66e37da2ae95f7d61a07f4b2567c3bb10bbb1b2ec953',
    #          '21',
    #          '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
    #          '21',
    #          '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
    #          '21',
    #          '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
    #          '21',
    #          '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
    #          '21',
    #          '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
    #          HEX_OPCODE['OP_6'],
    #          HEX_OPCODE['OP_CHECKMULTISIG']]
    #     h = ''.join(s)
    #     s = unhexlify(h)
    #     k = tools.parse_script(s)
    #     sh = tools.script_to_hash(h, 0, 0)
    #     self.assertEqual(k["type"],"NON_STANDARD")
    #     self.assertEqual(k["nType"],7)
    #     self.assertEqual(k["reqSigs"],1)
    #
    #     s = [HEX_OPCODE['OP_1'],
    #          HEX_OPCODE['OP_6'],
    #          '21',
    #          '021ecd2e5eb5dbd7c8e59f66e37da2ae95f7d61a07f4b2567c3bb10bbb1b2ec953',
    #          '21',
    #          '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
    #          '21',
    #          '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
    #          '21',
    #          '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
    #          '21',
    #          '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
    #          '21',
    #          '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
    #          HEX_OPCODE['OP_6'],
    #          HEX_OPCODE['OP_CHECKMULTISIG']]
    #     h = ''.join(s)
    #     s = unhexlify(h)
    #     k = tools.parse_script(s)
    #     self.assertEqual(k["type"], "NON_STANDARD")
    #     self.assertEqual(k["nType"], 7)
    #     self.assertEqual(k["reqSigs"], 6)
    #
    #     s = [HEX_OPCODE['OP_1'],
    #          HEX_OPCODE['OP_6'],
    #          '21',
    #          '021ecd2e5eb5dbd7c8e59f66e37da2ae95f7d61a07f4b2567c3bb10bbb1b2ec953',
    #          '21',
    #          '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
    #          '21',
    #          '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
    #          '21',
    #          '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
    #          '21',
    #          '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
    #          '21',
    #          '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
    #          HEX_OPCODE['OP_6'],
    #          HEX_OPCODE['OP_6'],
    #          HEX_OPCODE['OP_CHECKMULTISIG']]
    #     h = ''.join(s)
    #     s = unhexlify(h)
    #     k = tools.parse_script(s)
    #     self.assertEqual(k["type"],"NON_STANDARD")
    #     self.assertEqual(k["nType"],7)
    #     self.assertEqual(k["reqSigs"],20)
    #
    #     s = [HEX_OPCODE['OP_1'],
    #          HEX_OPCODE['OP_6'],
    #          '21',
    #          '021ecd2e5eb5dbd7c8e59f66e37da2ae95f7d61a07f4b2567c3bb10bbb1b2ec953',
    #          '21',
    #          '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
    #          '21',
    #          '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
    #          '21',
    #          '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
    #          '21',
    #          '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
    #          '21',
    #          '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
    #          HEX_OPCODE['OP_6'],
    #          HEX_OPCODE['OP_CHECKSIG'],
    #          HEX_OPCODE['OP_CHECKMULTISIG']]
    #     h = ''.join(s)
    #     s = unhexlify(h)
    #     k = tools.parse_script(s)
    #     self.assertEqual(k["type"],"NON_STANDARD")
    #     self.assertEqual(k["nType"],7)
    #     self.assertEqual(k["reqSigs"],21)
    #
    #
    #     s = [HEX_OPCODE['OP_1'],
    #          HEX_OPCODE['OP_6'],
    #          '21',
    #          '021ecd2e5eb5dbd7c8e59f66e37da2ae95f7d61a07f4b2567c3bb10bbb1b2ec953',
    #          '21',
    #          '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
    #          '21',
    #          '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
    #          '21',
    #          '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
    #          '21',
    #          '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
    #          '21',
    #          '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
    #          '21',
    #          '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
    #          HEX_OPCODE['OP_6'],
    #          HEX_OPCODE['OP_CHECKMULTISIG']]
    #     h = ''.join(s)
    #     s = unhexlify(h)
    #     k = tools.parse_script(s)
    #     self.assertEqual(k["type"],"NON_STANDARD")
    #     self.assertEqual(k["nType"],7)
    #     self.assertEqual(k["reqSigs"],20)
    #
    #     s = [
    #          HEX_OPCODE['OP_6'],
    #          '21',
    #          '021ecd2e5eb5dbd7c8e59f66e37da2ae95f7d61a07f4b2567c3bb10bbb1b2ec953',
    #          '21',
    #          '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
    #          '21',
    #          '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
    #          '21',
    #          '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
    #          '21',
    #          '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
    #          '21',
    #          '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
    #          '21',
    #          '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
    #          HEX_OPCODE['OP_6'],
    #          HEX_OPCODE['OP_CHECKMULTISIG']]
    #     h = ''.join(s)
    #     s = unhexlify(h)
    #     k = tools.parse_script(s)
    #     self.assertEqual(k["type"],"NON_STANDARD")
    #     self.assertEqual(k["nType"],7)
    #     self.assertEqual(k["reqSigs"],20)
    #
    #
    #     s = [
    #          HEX_OPCODE['OP_6'],
    #          '21',
    #          '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
    #          '21',
    #          '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
    #          '21',
    #          '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
    #          '21',
    #          '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
    #          '21',
    #          '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
    #          '21',
    #          '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
    #          HEX_OPCODE['OP_6'],
    #          HEX_OPCODE['OP_CHECKMULTISIG']]
    #     h = ''.join(s)
    #     s = unhexlify(h)
    #     k = tools.parse_script(s)
    #     self.assertEqual(k["type"],"MULTISIG")
    #     self.assertEqual(k["nType"],4)
    #     self.assertEqual(k["reqSigs"],6)
    #
    #
    #     s = [
    #          HEX_OPCODE['OP_1'],
    #          '21',
    #          '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
    #          '21',
    #          '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
    #          '21',
    #          '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
    #          '21',
    #          '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
    #          '21',
    #          '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
    #          '21',
    #          '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
    #          HEX_OPCODE['OP_6'],
    #          HEX_OPCODE['OP_CHECKMULTISIG']]
    #     h = ''.join(s)
    #     s = unhexlify(h)
    #     k = tools.parse_script(s)
    #     self.assertEqual(k["type"],"MULTISIG")
    #     self.assertEqual(k["nType"],4)
    #     self.assertEqual(k["reqSigs"],1)
    #
    #
    #
    #     s = [
    #          HEX_OPCODE['OP_1'],
    #          '21',
    #          '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
    #          '21',
    #          '02b63fe474a5daac88eb74fdc9ce0ec69a8f8b81d2d89ac8d518a2f54d4bcaf4a5',
    #          '21',
    #          '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
    #          '21',
    #          '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
    #          '21',
    #          '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
    #          HEX_OPCODE['OP_6'],
    #          HEX_OPCODE['OP_CHECKMULTISIG']]
    #     h = ''.join(s)
    #     s = unhexlify(h)
    #     k = tools.parse_script(s)
    #     self.assertEqual(k["type"],"NON_STANDARD")
    #     self.assertEqual(k["nType"],7)
    #     self.assertEqual(k["reqSigs"],20)
    #
    #
    #     s = [
    #          HEX_OPCODE['OP_1'],
    #          '21',
    #          '023bd78b0e7606fc1205721e4403355dfc0dbe4f1b15712cbbb17b1dc323cc8c0b',
    #          '21',
    #          '02afa49972b95496b39e7adc13437239ded698d81c85e9d029debb88641733528d',
    #          HEX_OPCODE['OP_DUP'],
    #          '21',
    #          '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
    #          '21',
    #          '03fedb540dd71a0211170b1857a3888d9f950231ecd0fcc7a37ffe094721ca151f',
    #          '21',
    #          '02fb394aaf232e114c06b1d1ca15f97602d2377c33e6fe5a1287421b09b08a5a3e',
    #          HEX_OPCODE['OP_6'],
    #          HEX_OPCODE['OP_CHECKMULTISIG']]
    #     h = ''.join(s)
    #     s = unhexlify(h)
    #     k = tools.parse_script(s)
    #     self.assertEqual(k["type"],"NON_STANDARD")
    #     self.assertEqual(k["nType"],7)
    #     self.assertEqual(k["reqSigs"],20)
    #
