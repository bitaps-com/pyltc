from pybtc.functions.tools import *

import types
import functools

def copy_function(f, scope):
    g = types.FunctionType(f.__code__, scope, name=f.__name__, argdefs=f.__defaults__,  closure=f.__closure__)
    g = functools.update_wrapper(g, f)
    g.__kwdefaults__ = f.__kwdefaults__
    return g