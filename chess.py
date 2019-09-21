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

def get_moves(move_type, board, row_position, col_position):
    # move types (h horizontal, v vertical, d diagonal, l L-shaped)
    possible_moves = []
    
    # Horizontal
    if (move_type == "h"):
        for idx, col in enumerate(board[row_position]):
            if (idx != 0 and idx != col_position):
                possible_moves.append(idx)
    
    if (move_type == "v"):
        # for idx, row in enumerate(board):
        for idx in range(10):
            print("LOOK IDX IS: " + str(idx))
            print("LOOK ROW POSITION IS: " + str(row_position))
            if (idx != row_position):
                print("NOOOOOO LOOK, IDX IS NOT ROW POSITION, IDX IS: " + str(idx))
                possible_moves.append(idx)
                #print("idx: " + str(idx))
                #print("row: " + str(row))
    #else:
        #print("Unsupported move type!: " + move_type)
        #exit(1)
    
    return possible_moves

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

# Print output from get_moves...
h_moves = get_moves("h", board, row_position, col_position)
for move in range(len(h_moves)):
    board[row_position][h_moves[move]] = "*"

#v_moves = get_moves("v",board, row_position, col_position)
#for move in range(len(v_moves)):
 #   board[move][col_position] = "+"

print_board(board)

# WHY IS Q GETTING OVERWRITTEN?