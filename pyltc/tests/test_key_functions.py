from pyltc.functions.tools import bytes_from_hex
import pytest

from pyltc.functions.key import create_private_key
from pyltc.functions.key import wif_to_private_key
from pyltc.functions.key import private_key_to_wif
from pyltc.functions.key import is_wif_valid
from pyltc.functions.key import private_to_public_key
from pyltc.functions.key import is_public_key_valid



def test_create_private_key():
    wk = create_private_key()
    k = wif_to_private_key(wk)
    assert private_key_to_wif(k) == wk
    wk = create_private_key(hex=True)
    assert len(wk) == 64
    wk = create_private_key(hex=False, wif = False)
    assert len(wk) == 32

def test_private_key_to_wif():
    assert private_key_to_wif("aaf19a8a8eacca26b2ec3678e47ee22a04fc1efac61bcd2a41af332be63bab8b",
                              compressed=0, testnet=0) == \
           "6vRJaVegzBxTXdgGEimmmSsEv1CLdAgfpaHsZbXUxkPfm9H8U7X";

    assert private_key_to_wif(bytes_from_hex("7fbda89e59e07db5897cabfde8eb8036d4bebdfddfeac97319e74c74c02799f2"),
                              compressed=1, testnet=0) == \
           "T7LHhPHG4mno7XPvBXajDrA5v2nLVSw16sTErD9y6Yki3bGTuHgf";

    assert private_key_to_wif("fc1528167b31735464059aef58cf71b501eaa146bae7e47f406c61f7ac28555c",
                              compressed=0, testnet=1) == \
           "93VwGxfztHBcUefSWA3JMzKsr6Jg4atmZdKvi1MXTgB9HLypXry";

    assert private_key_to_wif("fef231a9299de5b2d3ea012cd2471bdc80d38e489f5f4a7803ac3279a7d727a9",
                              compressed=1, testnet=1) == \
           "cW8HPuCThQ4EsLEU8S6Gborp7NfwXDc2uh2Aua83kmhjqN8GzEVk";

    with pytest.raises(TypeError):
        private_key_to_wif("ceda1ae4286015d45ec5147fe3f63e9377ccd6d4e98bcf0847df9937da1944")


def test_wif_to_private_key():
    wk = create_private_key(testnet=True)
    k = wif_to_private_key(wk)
    assert private_key_to_wif(k, testnet=True) == wk

    wk = create_private_key(compressed=False)
    k = wif_to_private_key(wk)
    assert private_key_to_wif(k, compressed=False) == wk

    wk = create_private_key(compressed=False, testnet=False)
    k = wif_to_private_key(wk)
    assert private_key_to_wif(k, compressed=False, testnet=False) == wk

    wk = create_private_key(compressed=False, testnet=True)
    k = wif_to_private_key(wk)
    assert private_key_to_wif(k, compressed=False, testnet=True) == wk

    p = "aaf19a8a8eacca26b2ec3678e47ee22a04fc1efac61bcd2a41af332be63bab8b"
    wif = "6vRJaVegzBxTXdgGEimmmSsEv1CLdAgfpaHsZbXUxkPfm9H8U7X"
    assert wif_to_private_key(wif, hex=1) == p

    p = "7fbda89e59e07db5897cabfde8eb8036d4bebdfddfeac97319e74c74c02799f2"
    wif = "T7LHhPHG4mno7XPvBXajDrA5v2nLVSw16sTErD9y6Yki3bGTuHgf"
    assert wif_to_private_key(wif, hex=1) == p

    p = "fc1528167b31735464059aef58cf71b501eaa146bae7e47f406c61f7ac28555c"
    wif = "93VwGxfztHBcUefSWA3JMzKsr6Jg4atmZdKvi1MXTgB9HLypXry"
    assert wif_to_private_key(wif, hex=1) == p

    p = "fef231a9299de5b2d3ea012cd2471bdc80d38e489f5f4a7803ac3279a7d727a9"
    wif = "cW8HPuCThQ4EsLEU8S6Gborp7NfwXDc2uh2Aua83kmhjqN8GzEVk"
    assert wif_to_private_key(wif, hex=1) == p

    with pytest.raises(TypeError):
        wif_to_private_key("L49obCXV7fGz2YRzLCSJgeZBYmGeBbKPT7xiehUeYX2S4URkPFqX")

def test_is_wif_valid():
    assert is_wif_valid("6vRJaVegzBxTXdgGEimmmSsEv1CLdAgfpaHsZbXUxkPfm9H8U7X") == True
    assert is_wif_valid("T7LHhPHG4mno7XPvBXajDrA5v2nLVSw16sTErD9y6Yki3bGTuHgf") == True
    assert is_wif_valid("T7LHh1HG4mno7XPvBXajDrA5v2nLVSw16sTErD9y6Yki3bGTuHgf") == False
    assert is_wif_valid("93VwGxfztHBcUefSWA3JMzKsr6Jg4atmZdKvi1MXTgB9HLypXry") == True
    assert is_wif_valid("93VwGxfztHBcUefSWA3JMzKsr6Jg4atmZdKvi1MXTgB9HLypXry") == True
    assert is_wif_valid("cW8HPwCThQ4EsLEU8S6Gborp7NfwXDc2uh2Aua83kmhjqN8GzEVk") == False
    assert is_wif_valid("5KPPLXhtga99qqMcWRo4Z6LXV3Kx6a9hRx3ez2U7EwP5K333Zfy2Wf") == False
    assert is_wif_valid("L49obCXV7fGz2YRzLCSJgeZqqBYmGeBbKPT7xiehUeYX2S4URkPFZX") == False
    assert is_wif_valid("cUWo47XLYtga99qqMcWRo4Z6LXV3Kx6a9hRx3ez2U7EwP5KZfy2Wf") == False
    assert is_wif_valid("cUWo47XLYiyFByuFi§FS3y4FAza3r3R5XA7Bm7wA3dgSKDY12oxQ7h9") == False
    assert is_wif_valid(22) == False


def test_private_to_public_key():
    priv = "ceda1ae4286015d45ec5147fe3f63e9377ccd6d4e98bcf0847df9937da1944a4"
    pu = "04b635dbdc16dbdf4bb9cf5b55e7d03e514fb04dcef34208155c7d3ec88e9045f4" \
         "c8cbe28702911260f2a1da099a338bed4ee98f66bb8dba8031a76ab537ff6663"
    pk = "03b635dbdc16dbdf4bb9cf5b55e7d03e514fb04dcef34208155c7d3ec88e9045f4"

    assert private_to_public_key(priv) == pk
    assert private_to_public_key(bytes_from_hex(priv)) == pk
    assert private_to_public_key(bytearray(bytes_from_hex(priv))) == pk
    assert private_to_public_key(priv) == pk
    assert private_to_public_key(priv, hex=True) == pk
    assert private_to_public_key(priv, hex=False).hex() == pk
    assert private_to_public_key(priv, compressed=False) == pu
    assert private_to_public_key("T9z52wpfX3FaoP4rsqPAu16ZVcuxFgLHGKryWW7C7VCbaN2pA6Tt", pk)
    assert private_to_public_key("6vh7ofFRazc2KDFUAFb2LV7hSWtRJNbjCdSphDV8xPhh1PrWTYt", pu)
    assert private_to_public_key("93A1vGXSGoDHotruGmgyRgtV8hgfFjgtmtuc4epcag886W9d44L", pu)
    assert private_to_public_key("cUWo47XLYiyFByuFicFS3y4FAza3r3R5XA7Bm7wA3dgSKDYox7h6", pk)
    with pytest.raises(ValueError):
        assert private_to_public_key("ceda1ae4286015d45ec5147fe3f63e9377ccd6d4e98bcf0847df9937da1944a411", pu)
    with pytest.raises(ValueError):
        private_to_public_key(3738)
    with pytest.raises(Exception):
        private_to_public_key("L49obCXV7fGz2YRzLCSJgeZBYmGeBbKPT7xiehUeYX2S4URkPFZQ")


def test_is_public_key_valid():
    pu = "04b635dbdc16dbdf4bb9cf5b55e7d03e514fb04dcef34208155c7d3ec88e9045f4" + \
         "c8cbe28702911260f2a1da099a338bed4ee98f66bb8dba8031a76ab537ff6663"
    pk = "03b635dbdc16dbdf4bb9cf5b55e7d03e514fb04dcef34208155c7d3ec88e9045f4"

    assert is_public_key_valid(pu) == True
    assert is_public_key_valid(pk) == True
    assert is_public_key_valid(bytes_from_hex(pk)) == True
    assert is_public_key_valid(bytes_from_hex(pu)) == True
    pu = "63qdbdc16dbdf4bb9cf45b55e7d03e514fb04dcef34208155c7d3ec88e9045f4c8c" + \
         "be28702911260f2a1da099a338bed4ee98f66bb8dba8031a76ab537ff6663"
    pk = "02b635dbdc16dbdf455bb9cf5b55e7d03e514fb04dcef34208155c7d3ec88e9045f4"

    assert is_public_key_valid(pu) == False
    assert is_public_key_valid(pk) == False
    assert is_public_key_valid("8989") == False

    pu = "04b635dbdc16dbdf455bb9cf5b55e7d03e514fb04dcef34208155c7d3ec88e902245f4"
    assert is_public_key_valid(pu) == False
