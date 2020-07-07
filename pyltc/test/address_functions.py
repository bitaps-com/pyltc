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





    def test_create_private_key(self):
        p = functions.create_private_key(wif=0)
        pw = functions.private_key_to_wif(p)
        self.assertEqual(functions.is_wif_valid(pw), True)


    #
    def test_private_to_public_key(self):
        p = "ceda1ae4286015d45ec5147fe3f63e9377ccd6d4e98bcf0847df9937da1944a4"
        pu = "04b635dbdc16dbdf4bb9cf5b55e7d03e514fb04dcef34208155c7d3ec88e9045f4c8cbe28702911260f2a1da099a338bed4ee98f66bb8dba8031a76ab537ff6663"
        pk = "03b635dbdc16dbdf4bb9cf5b55e7d03e514fb04dcef34208155c7d3ec88e9045f4"
        self.assertEqual(functions.private_to_public_key(p, hex=1), pk)
        self.assertEqual(functions.private_to_public_key(p, hex=0), unhexlify(pk))
        self.assertEqual(functions.private_to_public_key(p, compressed=0, hex=1), pu)

        self.assertEqual(functions.private_to_public_key("T9z52wpfX3FaoP4rsqPAu16ZVcuxFgLHGKryWW7C7VCbaN2pA6Tt", hex=1), pk)
        self.assertEqual(functions.private_to_public_key("6vh7ofFRazc2KDFUAFb2LV7hSWtRJNbjCdSphDV8xPhh1PrWTYt", hex=1), pu)
        self.assertEqual(functions.private_to_public_key("93A1vGXSGoDHotruGmgyRgtV8hgfFjgtmtuc4epcag886W9d44L", hex=1), pu)
        self.assertEqual(functions.private_to_public_key("cUWo47XLYiyFByuFicFS3y4FAza3r3R5XA7Bm7wA3dgSKDYox7h6", hex=1), pk)
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
    #
    # def test_parse_script(self):
    #
    #     k = tools.parse_script("76a9144b2832feeda5692c96c0594a6314136a998f515788ac")
    #     address = functions.hash_to_address(k["addressHash"], witness_version = None)
    #     # self.assertEqual(address, "17rPqUf4Hqu6Lvpgfsavt1CzRy2GL19GD3")
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
    #     address = functions.hash_to_address(k["addressHash"], script_hash=True, witness_version=None, legacy=True)
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
    #     # self.assertEqual(address, "bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4")
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
    #                                     witness_version=None, testnet=False, legacy=True)
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
    #                                     witness_version=None, testnet=False, legacy=True)
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
