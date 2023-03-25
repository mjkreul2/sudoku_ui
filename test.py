
from ctypes import *
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

# Initialize variable
test_array = _int_array_type()
ret_array = _int_pointer_type()

# print(test_array.contents)

for i in range(0,81) :
    test_array[i] = c_int(0)

print("original board")
for i in range(0,81) :
    print(test_array[i], end=" ")

print("")
print("solving board")
ret_array = _solve(cast(test_array, _int_pointer_type))

print("solved board")

for i in range(0,81) :
    print(ret_array[i], end=" ")

print()
for i in range(0,81) :
    print(test_array[i], end=" ")

_free(ret_array)
