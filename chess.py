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

# This function translates list positions to -> algebraic positions 
def get_list_position(r_heading, c_heading):
    # row heading/ outer list position
    row_mapping = {'1': 8, '2': 7, '3': 6, '4': 5, '5': 4, '6': 3, '7': 2, '8': 1 }
    # col heading/ inner list position
    col_mapping = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8 }
    row_list_pos = row_mapping[r_heading]
    col_list_pos = col_mapping[c_heading]
    return row_list_pos, col_list_pos

# Use this function to return back algebraic location of possible moves to user...
def get_board_position(r_heading, c_heading):
    row_mapping = {8: 1, 7: 2, 6: 3, 5: 4, 4: 5, 3: 6, 2: 7, 1: 8 }
    col_mapping = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h' }
    row_list_pos = row_mapping[r_heading]
    col_list_pos = col_mapping[c_heading]
    board_position =  str(col_list_pos) + str(row_list_pos)
    # print("HELLO FROM get_board_positions: board_position: " + board_position)
    return board_position

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


# execute h moves
h_moves = get_moves("h", board, row_position, col_position)
h_move_positions = []
for move in h_moves:
    board[row_position][move] = "h"
    list_position = int(str(row_position) + str(move))
    h_move_positions.append(list_position)

board_positions = []
for id, rp in enumerate(h_move_positions):
    row_p = int(str(rp)[0])
    col_p = int(str(rp)[1])
    board_positions.append(get_board_position(row_p, col_p))
# print("Look here are board_positions: " + str(board_positions))
   
# execute v moves
v_moves = get_moves("v",board, row_position, col_position)
for move in v_moves:
    board[move][col_position] = "v"

# LOOK
# work on this next, you want to append all the  possible v moves to board_positions list,
# right now it just has h_moves...*Do this from 1 function..
# for id, rp in enumerate(h_move_positions):
#    row_p = int(str(rp)[0])
#    col_p = int(str(rp)[1])
#    board_positions.append(get_board_position(row_p, col_p))
# print("Look here are board_positions: " + str(board_positions))

print_board(board)


print("Look here are board_positions: " + str(board_positions))