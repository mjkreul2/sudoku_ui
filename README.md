# sudoku_ui

This is a project that will provide a ui client for the sudoku solver made here: [Sudoku Solver](https://github.com/mjkreul2/sudoku_c/tree/pyinteg).

To input your own sudoku, simply input the numbers into the text box and press `Enter Sudoku`.  For custom sudoku puzzle inputs, `0` represents an empty space.

### How to run
1. Open terminal and move to the directory containing the python code
2. In the terminal type `python3 test.py`

### Windows Users
You may need to recompile the shared library (`libsudoku.so`) in order for python to be able to see the functions.
If so, do the following:
1. Navigate to https://github.com/mjkreul2/sudoku_c/tree/pyinteg
2. Clone repo to your personal machine
3. Navigate to `sudoku.h` and add `__declspec(dllexport)` in front of `parseIntPointer` and `freeIntPointer`. The header file should look like the following:
   ```
   __declspec(dllexport) int* parseIntPointer(int*);
   __declspec(dllexport) int* freeIntPointer(int*); 
   ```
4. Save the file
5. Now in your terminal do the following:
   ```Terminal
   $ make clean
   $ make shared 
   ```
6. Copy the created shared library (`libsudoku.so`) into the directory containing the python files

### *Things to do*:
- [x] Successfully create and solve a sudoku puzzle 
- [ ] Create UI interface 
- [x] Create wrapper libraries to more elegantly use the C shared library
- [ ] Reduce the amount of memory used by library
- [ ] Figure out how to add C Sudoku Solver to this repo so it is always up to date 
- [ ] Fix the C repo to be a fork of the old one 
- [ ] Add window to input users sudoku puzzle
- 
