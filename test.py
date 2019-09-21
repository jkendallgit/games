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

def get_position(r_heading, c_heading):
    # row heading/ outer list item position
    row_mapping = {'1': 8, '2': 7, '3': 6, '4': 7, '5': 4, '6': 3, '7': 3, '8': 1 }
    # col heading/ inner list item position
    col_mapping = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8 }
    row_list_pos = row_mapping[r_heading]
    col_list_pos = col_mapping[c_heading]
    print("Player is at " + r_heading + c_heading + " which is " + str(row_list_pos) + "," + str(col_list_pos))

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

# print initialized board...
print_board(board)

# User input would be 2d...

# given user input, call get_position to return the outer and inner list locations...
get_position("2", "d")

# Given list coordinates that get_position returns, put a player on the board at that position
# -piece KNIGHT -position d2

board[7][4] = "K"

# re-draw the board...
print_board(board)
