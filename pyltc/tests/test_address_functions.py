import pytest
from pyltc.functions.address import hash_to_address
from pyltc.functions.address import address_to_hash
from pyltc.functions.address import public_key_to_address
from pyltc.functions.address import address_type
from pyltc.functions.address import address_net_type
from pyltc.functions.address import is_address_valid
from pyltc.functions.address import get_witness_version

def test_public_key_to_address():
    pc = "032b4cc0e17e9170eb8f264514d95226f11cfef53c829fead8e0589d64b0640614"
    assert public_key_to_address(pc,
                                 witness_version=None,
                                 testnet=False) == "Lg7snsFMmPnqHfKV6kSw599vE4bMV1xqhr"
    with pytest.raises(ValueError):
        public_key_to_address(pc + "33", p2sh_p2wpkh=True)
    with pytest.raises(ValueError):
        public_key_to_address(pc + "33", witness_version=0)


def test_hash_to_address():
    # p2wpkh
    h = "751e76e8199196d454941c45d1b3a323f1433bd6"
    assert hash_to_address(h) == "ltc1qw508d6qejxtdg4y5r3zarvary0c5xw7kgmn4n9"
    # p2wsh
    h = "1863143c14c5166804bd19203356da136c985678cd4d27a1b8c6329604903262"
    assert hash_to_address(h, testnet=1) == \
                     "tltc1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qsnr4fp"
    # p2sh
    h = "014f2e7072e9907c7f636d937759b8ceb1053feb"
    assert hash_to_address(h, testnet=0, witness_version=None, script_hash=True) == \
                     "M825mF1bLC3hPL6ZmaEVqZ2pouU5iRE72D"
    # p2pkh
    h = "d421ce551279f3fdfb6e4f7390b06516c3daaaa2"
    assert  hash_to_address(h, testnet=0, witness_version=None) == \
                     "LeZc1mA2SgaNTJ4WE8pKegNKbZekqovqvK"


def test_address_to_hash():
    assert  address_to_hash("ltc1qw508d6qejxtdg4y5r3zarvary0c5xw7kgmn4n9", 1) == \
                     "751e76e8199196d454941c45d1b3a323f1433bd6"

    assert  address_to_hash("tltc1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qsnr4fp", 1) == \
                     "1863143c14c5166804bd19203356da136c985678cd4d27a1b8c6329604903262"

    assert  address_to_hash("M825mF1bLC3hPL6ZmaEVqZ2pouU5iRE72D", 1) == \
                     "014f2e7072e9907c7f636d937759b8ceb1053feb"

    assert  address_to_hash("LeZc1mA2SgaNTJ4WE8pKegNKbZekqovqvK", 1) == \
                     "d421ce551279f3fdfb6e4f7390b06516c3daaaa2"


def test_address_type():
    assert address_type("ltc1qw508d6qejxtdg4y5r3zarvary0c5xw7kgmn4n9"), 'P2WPKH'
    assert address_type("tltc1q8qwavl6pg95r2hjvajqr3tu5ac0q4eeu73vh7r"), 'P2WPKH'
    assert address_type("tltc1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qsnr4fp"), 'P2WSH'
    assert address_type("ltc1qy4rwhdkujk35ga26774gqmng67kgggtqnsx9vp0xgzp3wz3yjkhqashszw"), 'P2WSH'
    assert address_type("tltc1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qsnr4fp"), 'P2WSH'
    assert address_type("LeZc1mA2SgaNTJ4WE8pKegNKbZekqovqvK"), 'P2PKH'
    assert address_type("33am12q3Bncnn3BfvLYHczyv23Sq2Wbwjw"), 'P2SH'
    assert address_type("M825mF1bLC3hPL6ZmaEVqZ2pouU5iRE72D"), 'P2SH'

def test_address_net_type():
    assert address_net_type("ltc1qw508d6qejxtdg4y5r3zarvary0c5xw7kgmn4n9") == 'mainnet'
    assert address_net_type("tltc1q8qwavl6pg95r2hjvajqr3tu5ac0q4eeu73vh7r") == 'testnet'
    assert address_net_type("ltc1qy4rwhdkujk35ga26774gqmng67kgggtqnsx9vp0xgzp3wz3yjkhqashszw") == 'mainnet'
    assert address_net_type("tltc1qcmdwjnv7yv6csp3ft8xw06jzvkzgl8xvjv5wdn85nefqpq3m29rs5ykqy4") =='testnet'
    assert address_net_type("LeZc1mA2SgaNTJ4WE8pKegNKbZekqovqvK") == 'mainnet'
    assert address_net_type("mipcBbFg9gMiCh81Kj8tqqdgoZub1ZJRfn") == 'testnet'
    assert address_net_type("3MSvaVbVFFLML86rt5eqgA9SvW23upaXdY") == 'mainnet'
    assert address_net_type("MTf4tP1TCNBn8dNkyxeBVoPrFCcVzxJvvh") == 'mainnet'
    assert address_net_type("2N2PJEucf6QY2kNFuJ4chQEBoyZWszRQE16") == 'testnet'
    assert address_net_type("QVk4MvUu7Wb7tZ1wvAeiUvdF7wxhvpyLLK") == 'testnet'


def test_is_address_valid():
    assert is_address_valid("ltc1qw508d6qejxtdg4y5r3zarvary0c5xw7kgmn4n9", 0) == True
    assert is_address_valid("tltc1q8qwavl6pg95r2hjvajqr3tu5ac0q4eeu73vh7r", 1) == True
    assert is_address_valid("tltc1q8qwavm6pg95r2hjvajqr3tu5ac0q4eeu73vh7r") == False
    assert is_address_valid("ltc1qy4rwhdkujk35ga26774gqmng67kgggtqnsx9vp0xgzp3wz3yjkhqashszw") == True
    assert is_address_valid("tltc1qcmdwjnv7yv6csp3ft8xw06jzvkzgl8xvjv5wdn85nefqpq3m29rs5ykqy4",1) == True
    assert is_address_valid("LeZc1mA2SgaNTJ4WE8pKegNKbZekqovqvK") == True
    assert is_address_valid("mvNyptwisQTmwL3vN8VMaVUrA3swVCX83c", 1) == True
    assert is_address_valid("33am12q3Bncnn3BfvLYHczyv23Sq2Wbwjw") == True
    assert is_address_valid("2Mu8y4mm4oF88yppDbUAAEwyBEPezrx7CLh", 1) == True
    assert is_address_valid("2Mu8y4mm4oF89yppDbUAAEwyBEPezrx7CLh", 1) == False
    assert is_address_valid("M825mF1bLC3hPL6ZmaEVqZ2pouU5iRE72D", 0) == True
    assert is_address_valid("QVk4MvUu7Wb7tZ1wvAeiUvdF7wxhvpyLLK", 1) == True
    assert is_address_valid("1Fs2Xqrk4P2XADaJeZWykaGXJ2HEb6RyT1") == False
    assert is_address_valid("mvNyptwisQTkwL3vN8VMaVUrA3swVCX83c", 1)== False
    assert is_address_valid("33am12q3Bncmn3BfvLYHczyv23Sq2Wbwjw") == False
    assert is_address_valid("2Mu8y4mm4oF78yppDbUAAEwyBEPezrx7CLh", 1) == False


def test_get_witness_version():
    assert get_witness_version("ltc1qy4rwhdkujk35ga26774gqmng67kgggtqnsx9vp0xgzp3wz3yjkhqashszw") == 0
