from pyltc._isolation import specialize as _specialize
from pyltc.transaction import Transaction

Block = _specialize("pybtc.classes.block", __name__, {"Transaction": Transaction}).Block
