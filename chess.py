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

# Use this function to translate user input (algebraic position) to list positions for the game board..
def get_list_position(r_heading, c_heading):
    # row heading/ outer list position
    row_mapping = {'1': 8, '2': 7, '3': 6, '4': 5, '5': 4, '6': 3, '7': 2, '8': 1 }
    # col heading/ inner list position
    col_mapping = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8 }
    row_list_pos = row_mapping[r_heading]
    col_list_pos = col_mapping[c_heading]
    return row_list_pos, col_list_pos

# There must be a better way to do this, TODO combine this function with get_list_position
# and just reverse the dict instead of creating more dicts...
# Use this function to return back algebraic location of possible moves to user...
def get_board_position(r_heading, c_heading):
    row_mapping = {'8': 1, '7': 2, '6': 3, '5': 4, '4': 5, '3': 6, '2': 7, '1': 8 }
    col_mapping = {'1': a, '2': b, '3': c, '4': d, '5': e, '6': f, '7': g, '8': h }
    row_list_pos = row_mapping[r_heading]
    col_list_pos = col_mapping[c_heading]
    print("HELLO FROM get_board_positions: row_list_pos: " + row_list_pos)
    print("HELLO FROM get_board_positions: col_list_pos: " + col_list_pos)
    # return row_list_pos, col_list_pos

def get_moves(move_type, board, row_position, col_position):
    # move types (h horizontal, v vertical, d diagonal, l L-shaped)
    possible_moves = []
    
    # Horizontal
    if (move_type == "h"):
        for idx, col in enumerate(board[row_position]):
            if (idx > 0 and idx != col_position):
                possible_moves.append(idx)

    if (move_type == "v"):
        for idx, row in enumerate(board):
            if (idx > 0 and idx != row_position):
                possible_moves.append(idx)
    # Need to add a check here for any move type that's not supported..
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

# given user input, call get_list_position to return the outer and inner list locations...
row_position, col_position = get_list_position(input_position[1], input_position[0])
board[row_position][col_position] = input_piece

# Draw board with player's piece in position they specified..
print_board(board)

# execute h moves
h_moves = get_moves("h", board, row_position, col_position)
h_move_positions = []
for move in h_moves:
    board[row_position][move] = "h"
    list_position = int(str(row_position) + str(move))
    h_move_positions.append(list_position)
print("Look here is h_move_positions: " + str(h_move_positions))
# Look here is h_move_positions: [41, 42, 44, 45, 46, 47, 48]
return_to_user_positions = []
for id, rp in enumerate(h_move_positions):
    #get_board_position(h_move_positions[idx][0], h_move_positions[idx][1])
    print (int(str(rp)[0]))
    print (int(str(rp)[1]))
   


# execute v moves
v_moves = get_moves("v",board, row_position, col_position)
for move in v_moves:
    board[move][col_position] = "v"

# Next, let's try to add h_moves and v_moves lists together into a new list and re-draw
# the board based on that new list...

print_board(board)

#print("h move positions: " + h_move_positions)

#print(h_moves)
#print(v_moves)
#print(d_moves)
#print(l_moves)