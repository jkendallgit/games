# Draw Chess Board (this needs to turn into a function)
def print_board(board):
    for i in range(len(board)):
        if i > 0:
            print("   ---  ---  ---  ---  ---  ---  ---  ---")
        for j in range(len(board[i])):
            if i > 0 and j > 0:
                print(" |" + board[i][j] + "|", end = ' ')
            else:
                print(board[i][j], end = ' ')
        print()

def get_position(row, col):
    # row heading/ outer list item position
    row_heading = {'1': 8, '2': 7, '3': 6, '4': 7, '5': 4, '6': 3, '7': 3, '8': 1 }
    print(row_heading['3'])

    # col heading/ inner list item position
    col_heading = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8 }
    print(col_heading['c'])
 
    print("hi from get_position: " + row + col)

# Initialize chess board

board = [[" ", "  a", "   b", "   c", "   d", "   e", "   f", "   g", "   h"],
["8", " ", " ", " ", " ", " ", " ", " ", " "],
["7", " ", " ", " ", " ", " ", " ", " ", " "],
["6", " ", " ", " ", " ", " ", " ", " ", " "],
["5", " ", " ", " ", " ", " ", " ", " ", " "],
["4", " ", " ", " ", " ", " ", " ", " ", " "],
["3", " ", " ", " ", " ", " ", " ", " ", " "],
["2", " ", " ", " ", " ", " ", " ", " ", " "],
["1", " ", " ", " ", " ", " ", " ", " ", " "]]

# Next step, given an input coordinate like "d2", Draw a "K" as an item at that location within the list matrix.
#Do mappingin 2 steps, 2nd param passed in, like "2" will map to the "7th item in first (row) list,
# and then the 1st param that got passed in, like "d" will map to the 4th item in second (col) list.

get_position("2", "d")
# -piece KNIGHT -position d2
#mylist[7][4] = "K" #d2
#print(mylist[7][4])
# print_board(board)