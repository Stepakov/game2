import random

MAX_ROW_IN_THE_HEAP = 3
MAX_STONES_IN_A_ROW = 20

_holder = {}
_sorted_keys = None

def set_heap():
    global _holder, _sorted_keys
    _holder = {}
    for i in range( 1, MAX_ROW_IN_THE_HEAP + 1 ):
        _holder[ i ] =  random.randint( 1, MAX_STONES_IN_A_ROW )
    _sorted_keys = sorted( _holder.keys() )

def get_heap():
    res = []
    for num in _sorted_keys:
        res.append( _holder[ num ] )

    return res

def get_from_heap( position, quantity ):
    if position in _holder:
        _holder[ position ] -= quantity
        if( _holder[ position ] < 0 ): _holder[ position ] = 0
        return True
    else: return False

def is_gameover():
    return not any( _holder.values() )