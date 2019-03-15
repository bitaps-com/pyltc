import pybtc as __parent__
import pyltc.constants as constants
names = getattr(constants, '__all__', [n for n in dir(constants) if not n.startswith('_')])
[setattr(__parent__, name, getattr(constants, name)) for name in names]

import pyltc.opcodes as opcodes
names = getattr(opcodes, '__all__', [n for n in dir(opcodes) if not n.startswith('_')])
[setattr(__parent__, name, getattr(opcodes, name)) for name in names]

from pyltc.functions.tools import  rh2s
from pyltc.functions.script import decode_script
from pyltc.functions.address import  hash_to_address, address_net_type, address_to_script
from .address import  Address, ScriptAddress

setattr(__parent__.transaction, "address_net_type", address_net_type)
setattr(__parent__.transaction, "address_to_script", address_to_script)
setattr(__parent__.transaction, "address_to_script", address_to_script)
setattr(__parent__.transaction, "Address", Address)
setattr(__parent__.transaction, "ScriptAddress", ScriptAddress)

class Transaction(__parent__.Transaction):
    def decode1(self, testnet=None, legacy=False):
        """
        change Transaction object representation to "decoded" human readable format

        :param bool testnet: (optional) address type for "decoded" transaction representation, by default None.
                            if None used type from transaction property "format".
        """
        if self["format"] == "decoded":
            self.encode()
        self["format"] = "decoded"
        if testnet is not None:
            self["testnet"] = testnet
        if type(self["txId"]) == bytes:
            self["txId"] = rh2s(self["txId"])
        if "flag" in self:
            if type(self["flag"]) == bytes:
                self["flag"] = rh2s(self["flag"])
        if type(self["hash"]) == bytes:
            self["hash"] = rh2s(self["hash"])
        if type(self["rawTx"]) == bytes:
            self["rawTx"] = self["rawTx"].hex()
        for i in self["vIn"]:
            if type(self["vIn"][i]["txId"]) == bytes:
                self["vIn"][i]["txId"] = rh2s(self["vIn"][i]["txId"])
            if type(self["vIn"][i]["scriptSig"]) == bytes:
                self["vIn"][i]["scriptSig"] = self["vIn"][i]["scriptSig"].hex()
            try:
                t = list()
                append = t.append
                for w in self["vIn"][i]["txInWitness"]:
                    if type(w) == bytes:
                        w = w.hex()
                    append(w)
                self["vIn"][i]["txInWitness"] = t

            except:
                pass
            try:
                if type(self["vIn"][i]["addressHash"]) == bytes:
                    self["vIn"][i]["addressHash"] = self["vIn"][i]["addressHash"].hex()
                sh = True if self["vIn"][i]["nType"] in (1, 5) else False
                witness_version = None if self["vIn"][i]["nType"] < 5 else 0
                self["vIn"][i]["address"] = hash_to_address(self["vIn"][i]["addressHash"],
                                                            self["testnet"],
                                                            sh,
                                                            witness_version, legacy=legacy)
            except:
                pass
            if "scriptPubKey" in self["vIn"][i]:
                if type(self["vIn"][i]["scriptPubKey"]) == bytes:
                    self["vIn"][i]["scriptPubKey"] = self["vIn"][i]["scriptPubKey"].hex()
                self["vIn"][i]["scriptPubKeyOpcodes"] = decode_script(self["vIn"][i]["scriptPubKey"])
                self["vIn"][i]["scriptPubKeyAsm"] = decode_script(self["vIn"][i]["scriptPubKey"], 1)
            if "redeemScript" in self["vIn"][i]:
                if type(self["vIn"][i]["redeemScript"]) == bytes:
                    self["vIn"][i]["redeemScript"] = self["vIn"][i]["redeemScript"].hex()
                self["vIn"][i]["redeemScriptOpcodes"] = decode_script(self["vIn"][i]["redeemScript"])
                self["vIn"][i]["redeemScriptAsm"] = decode_script(self["vIn"][i]["redeemScript"], 1)
            if not self["coinbase"]:
                if type(self["vIn"][i]["scriptSig"]) == bytes:
                    self["vIn"][i]["scriptSig"] = self["vIn"][i]["scriptSig"].hex()
                self["vIn"][i]["scriptSigOpcodes"] = decode_script(self["vIn"][i]["scriptSig"])
                self["vIn"][i]["scriptSigAsm"] = decode_script(self["vIn"][i]["scriptSig"], 1)

        for i in self["vOut"]:
            if type(self["vOut"][i]["scriptPubKey"]) == bytes:
                self["vOut"][i]["scriptPubKey"] = self["vOut"][i]["scriptPubKey"].hex()
            try:
                if type(self["vOut"][i]["addressHash"]) == bytes:
                    self["vOut"][i]["addressHash"] = self["vOut"][i]["addressHash"].hex()
                sh = True if self["vOut"][i]["nType"] in (1, 5) else False
                witness_version = None if self["vOut"][i]["nType"] < 5 else 0
                self["vOut"][i]["address"] = hash_to_address(self["vOut"][i]["addressHash"],
                                                             self["testnet"],
                                                             sh,
                                                             witness_version, legacy=legacy)
            except:
                pass
            self["vOut"][i]["scriptPubKeyOpcodes"] = decode_script(self["vOut"][i]["scriptPubKey"])
            self["vOut"][i]["scriptPubKeyAsm"] = decode_script(self["vOut"][i]["scriptPubKey"], 1)
        if "data" in self:
            if type(self["data"]) == bytes:
                self["data"] = self["data"].hex()
        return self

