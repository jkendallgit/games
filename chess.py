import argparse

# Parse user input
parser = argparse.ArgumentParser()
parser.add_argument('-piece', required=True)
parser.add_argument('-position', required=True)
args = parser.parse_args()
input_piece = args.piece
input_position = args.position

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
    # row heading/ outer list position
    row_mapping = {'1': 8, '2': 7, '3': 6, '4': 5, '5': 4, '6': 3, '7': 2, '8': 1 }
    # col heading/ inner list position
    col_mapping = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8 }
    row_list_pos = row_mapping[r_heading]
    col_list_pos = col_mapping[c_heading]
    return row_list_pos, col_list_pos

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

# given user input, call get_position to return the outer and inner list locations...
row_position, col_position = get_position(input_position[1], input_position[0])
board[row_position][col_position] = input_piece

# Draw board with player's piece in position they specified..
print_board(board)

# Rook - can move any number of vacant squares vertically or horizontally. ..
    # Given row_position - print the possible out list index positions to left or right
        # of the current index ..  
    # Given col position - 
# To start, just print current position in the row (outer list)..
# board[row_position][col_position] = input_piece

# Just print out all item locations on current row except for 0 (that's a heading) and the current
# position, since it's already taken..
print("Row Position: " + str(row_position))
print("Col Position: " + str(col_position))
for c in range(len(board[row_position])):
    if (row_position != 0) and col_position: # and col_position != 0 and c != board[row_position][col_position]):
        print("cell content: " + board[row_position][c])

 

# Queen - can move any number of vacant squares diagonally, horizontally, or vertically.
# Knight - moves to a square that is two squares away horizontally and one square vertically, 
#           or two squares vertically and one square horizontally


