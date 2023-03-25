from sud_sol_wrapper import *
from tkinter import *

root = Tk()
root.title("Sudoku Solver")
# root.geometry("500x500")
board = StringVar()

board_box = Label(root, width=38, height=13, textvariable=board, justify=LEFT, font=('Courier', 14))
board_box.grid(row=5, column=0)

# text_box = Text(root, width=38,height=13)
# text_box.grid(row=4,column=0)

frm = Frame(root)


def print_board(arr=np.zeros(shape=(9, 9), dtype=int)) :
    str_to_add = ""
    # text_box.delete(1.0, "end-1c")
    # text_box.insert(index="end-1c",chars="-------------------------------------\n")
    str_to_add += "-------------------------------------\n"
    print("-------------------------------------")
    l = 1
    for i in range(0,9) :
        # text_box.insert(index="end-1c", chars="| ")
        str_to_add +="| "
        print("| ",end="")
        k = 1
        for j in range(0,9) :
            if (arr[i][j] < 1) :
                # text_box.insert(index="end-1c", chars=" _ ")
                str_to_add += " _ "
                print(" _ ", end="")
            else :
                # text_box.insert(index="end-1c", chars=" " + str(arr[i][j]) + " ")
                str_to_add += " " + str(arr[i][j]) + " "
                print(" " + str(arr[i][j]) + " ",end="")
            # end if
            if (k % 3 == 0) :
                # text_box.insert(index="end-1c", chars=" | ")
                str_to_add += " | "
                print(" | ", end="")
            #end if
            k+=1
        #end for
        # text_box.insert(index="end-1c", chars="\n")
        str_to_add += "\n"
        print()
        if (l%3==0) :
            # text_box.insert(index="end-1c",chars="-------------------------------------\n")
            str_to_add += "-------------------------------------\n"
            print("-------------------------------------")
        #end if
        l+=1
    #end for
    board.set(str_to_add)

def read_input(str=None) :
    if str==None :
        pass


def reset_box() :
    print_board()

def hello_world() :
    print("Hello, World!")

def enter_button() :
    pass

def run_test() :
    test_array = solve(np.zeros(shape=(9, 9), dtype=int))
    print()
    print("Output via python:")
    print()
    print_board(test_array)


frm.grid()
print_board()
Label(frm, text="Hello World!").grid(column=0, row=0)

Button(frm, text="Quit", command=root.destroy, cursor="center_ptr", bg="#51A0D5",activeforeground="#FF0000").grid(sticky=E,column=3,row=0)
Button(frm, text="hello", command=hello_world).grid(sticky=E,column=3,row=1)
Button(frm, text="run test", command=run_test).grid(sticky=E,column=3,row=2)
Button(frm, text="reset test", command=reset_box).grid(sticky=E,column=3,row=3)
root.mainloop()