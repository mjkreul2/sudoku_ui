# This is a library wrapper for the shared C library

from ctypes import *

import numpy as np

# Import the sudoku solver library
_sud_lib=cdll.LoadLibrary("./libsudoku.so")

# ctypes declarations
_int_array_type = c_int * 81
_int_pointer_type = POINTER(c_int)

# Creating instances of shared library functions
_solve = _sud_lib.parseIntPointer
_free = _sud_lib.freeIntPointer

# setting the inputs and return types
_solve.argtypes = [_int_pointer_type]
_solve.restype = _int_pointer_type
_free.argtypes = [_int_pointer_type]
_free.restype = None

def create_intp_from_array(arr: np.array) -> _int_array_type:
    """

    :param arr:
    :return:
    """
    # initialize return variable
    to_ret = _int_array_type()

    #copy over values
    i = 0
    for j in range(0,81) :
        to_ret[j] = arr[i][j%9]
        if (j%9==8) :
            i+=1

    return to_ret

def create_array_from_intp(intp: _int_pointer_type) -> np.array:
    """

    :param intp:
    :return:
    """
    to_ret = np.zeros(shape=(9,9), dtype=int)
    i = 0
    for j in range(0,81) :
        to_ret[i][j%9] = intp[j]
        if (j%9==8) :
            i+=1

    #now don't forget to free mem
    _free(intp)
    return to_ret

def solve(arr: np.array) -> np.array :
    """

    :param arr:
    :return:
    """

    # First, pass in our np.array and get an int array
    to_send = create_intp_from_array(arr)
    ret_array = _solve(cast(to_send, _int_pointer_type))
    arr = create_array_from_intp(ret_array)

    return(arr)


