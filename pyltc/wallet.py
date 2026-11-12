from pyltc._isolation import specialize as _specialize
import pyltc.constants as _constants
import pyltc.functions.bip32 as _bip32

Wallet = _specialize("pybtc.classes.wallet", __name__,
                     _constants, _bip32.__parent__).Wallet
