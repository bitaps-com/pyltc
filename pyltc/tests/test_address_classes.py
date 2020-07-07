import pytest
from pyltc.classes.address import PrivateKey
from pyltc.classes.address import PublicKey
from pyltc.classes.address import Address
from pyltc.classes.address import ScriptAddress

def test_PrivateKey_class():
    # mainnet
    assert PrivateKey("7fbda89e59e07db5897cabfde8eb8036d4bebdfddfeac97319e74c74c02799f2",
                       compressed=True, testnet=False).wif == \
                     'T7LHhPHG4mno7XPvBXajDrA5v2nLVSw16sTErD9y6Yki3bGTuHgf'
    assert PrivateKey("aaf19a8a8eacca26b2ec3678e47ee22a04fc1efac61bcd2a41af332be63bab8b",
                       compressed=False, testnet=False).wif == \
                     '6vRJaVegzBxTXdgGEimmmSsEv1CLdAgfpaHsZbXUxkPfm9H8U7X'
    # # testnet
    assert PrivateKey("fef231a9299de5b2d3ea012cd2471bdc80d38e489f5f4a7803ac3279a7d727a9",
                      compressed=True, testnet=True).wif == \
                     'cW8HPuCThQ4EsLEU8S6Gborp7NfwXDc2uh2Aua83kmhjqN8GzEVk'
    assert PrivateKey("fc1528167b31735464059aef58cf71b501eaa146bae7e47f406c61f7ac28555c",
                       compressed=False, testnet=True).wif == \
                     '93VwGxfztHBcUefSWA3JMzKsr6Jg4atmZdKvi1MXTgB9HLypXry'

    assert PrivateKey("cW8HPuCThQ4EsLEU8S6Gborp7NfwXDc2uh2Aua83kmhjqN8GzEVk",
                    compressed=False, testnet=True).wif == \
                     'cW8HPuCThQ4EsLEU8S6Gborp7NfwXDc2uh2Aua83kmhjqN8GzEVk'

def test_Address_class():
    p = PrivateKey("7b56e2b7bd189f4491d43a1d209e6268046df1741f61b6397349d7aa54978e76")
    pub = PublicKey(p)
    a = Address(p)
    a = Address(p, address_type="P2SH_P2WPKH", legacy=True)
    assert a.address == '37WJdFAoHDbxUQioDgtvPZuyJPyrrNQ7aL'
    assert a.redeem_script_hex == '001434370a8d74e9965d7aade2ba2f30110b321bf236'
    assert a.public_key.hex == '02a8fb85e98c99b79150df12fde488639d8445c57babef83d53c66c1e5c818eeb4'


    cpk = "02a8fb85e98c99b79150df12fde488639d8445c57babef83d53c66c1e5c818eeb4"
    ucpk = "04a8fb85e98c99b79150df12fde488639d8445c57babef83d53c66c1e5c818eeb" \
           "43bbd96a641808e5f34eb568e804fe679de82de419e2512736ea09013a82324a6"


    assert PublicKey("7b56e2b7bd189f4491d43a1d209e6268046df1741f61b6397349d7aa54978e76",
                     compressed=False).hex ==  ucpk
    # public key compressed from HEX private
    assert PublicKey("7b56e2b7bd189f4491d43a1d209e6268046df1741f61b6397349d7aa54978e76",
                     compressed=True).hex == cpk


    p = PublicKey('02a8fb85e98c99b79150df12fde488639d8445c57babef83d53c66c1e5c818eeb4')
    a = Address(p, address_type="P2SH_P2WPKH", legacy=True)
    assert a.address == '37WJdFAoHDbxUQioDgtvPZuyJPyrrNQ7aL'
    assert a.redeem_script_hex == '001434370a8d74e9965d7aade2ba2f30110b321bf236'
    assert a.public_key.hex == '02a8fb85e98c99b79150df12fde488639d8445c57babef83d53c66c1e5c818eeb4'


    redeem = "5221032bfc25cf7cccc278b26473e2967b8fd403b4b544b836e71abdfebb08d8c96d6921032bfc25cf7cccc278b2" \
             "6473e2967b8fd403b4b544b836e71abdfebb08d8c96d6921032bfc25cf7cccc278b26473e2967b8fd403b4b544b8" \
             "36e71abdfebb08d8c96d6953ae"
    a = ScriptAddress(redeem, witness_version=None, legacy=True)
    assert a.address == '3KCqqS6eznp3ucVPxtNkiYcVg6kQKNX9sg'
