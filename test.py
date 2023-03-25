from sud_sol_wrapper import *
from tkinter import *

root = Tk()
root.title("Sudoku Solver")
# root.geometry("500x500")

# Board Display
board = StringVar()
board_box = Label(root, width=38, height=13, textvariable=board, justify=LEFT, font=('Courier', 14))
board_box.grid(row=4, column=0)

# Text input
text_box = Text(root, width=9,height=9)
text_box.grid(row=5,column=0)

frm = Frame(root)

# Menu Button
# mb = Menubutton()
# menu = Menu(mb)


def print_board(arr=np.zeros(shape=(9, 9), dtype=int)) :
    str_to_add = ""
    # text_box.delete(1.0, "end-1c")
    # text_box.insert(index="end-1c",chars="-------------------------------------\n")
    str_to_add += "-------------------------------------\n"
    l = 1
    for i in range(0,9) :
        # text_box.insert(index="end-1c", chars="| ")
        str_to_add +="| "
        k = 1
        for j in range(0,9) :
            if (arr[i][j] < 1) :
                # text_box.insert(index="end-1c", chars=" _ ")
                str_to_add += " _ "
            else :
                # text_box.insert(index="end-1c", chars=" " + str(arr[i][j]) + " ")
                str_to_add += " " + str(arr[i][j]) + " "
            # end if
            if (k % 3 == 0) :
                # text_box.insert(index="end-1c", chars=" | ")
                str_to_add += " | "
            #end if
            k+=1
        #end for
        # text_box.insert(index="end-1c", chars="\n")
        str_to_add += "\n"
        print()
        if (l%3==0) :
            # text_box.insert(index="end-1c",chars="-------------------------------------\n")
            str_to_add += "-------------------------------------\n"
        #end if
        l+=1
    #end for
    board.set(str_to_add)

def read_input() :
    board_str = text_box.get(index1="1.0",index2=END)
    print(board_str)
    board_arr = change_text_board_to_array(board_str)
    print(board_arr)
    solved_board = solve_input(board_arr)
    print_board(solved_board)

def change_text_board_to_array(string : str) -> np.array :
    # first scrub the string
    if len(string) != 0 :
        string.replace('\n',"")

    end = len(string)
    if len(string) > 81 :
        end = 81
    to_ret = np.zeros(shape=(9,9), dtype=int)
    i = 0
    for j in range(0,end) :
        to_ret[i][j%9] = int(string[j])
        if(j%9==8):
            i+=1

    return to_ret

def reset_box() :
    print_board()

def hello_world() :
    print("Hello, World!")

def enter_button() :
    pass

def solve_input(input=np.zeros(shape=(9, 9), dtype=int)) -> np.array:
    to_ret = solve(input)
    return to_ret

def run_test() :
    test_array = solve(np.zeros(shape=(9, 9), dtype=int))
    print()
    print("Output via python:")
    print()
    print_board(test_array)


frm.grid(columnspan=5, rowspan=5)
print_board()
Label(frm, text="Enter Sudoku Above").grid(column=0, row=0)
Button(frm, text="Quit", command=root.destroy, cursor="center_ptr", bg="#51A0D5",activeforeground="#FF0000").grid(sticky=E,column=5,row=0)
Button(frm, text="Enter Sudoku", command=read_input).grid(sticky=E,column=5,row=1)
Button(frm, text="run test", command=run_test).grid(sticky=E,column=5,row=2)
Button(frm, text="reset test", command=reset_box).grid(sticky=E,column=5,row=3)
root.mainloop()