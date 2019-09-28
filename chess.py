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

# This function translates algebraic positions to ->  list positions 
def get_list_position(r_heading, c_heading):
    # r_heading = outer list position
    row_mapping = {'1': 8, '2': 7, '3': 6, '4': 5, '5': 4, '6': 3, '7': 2, '8': 1 }
    # c_heading = inner list position
    col_mapping = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8 }
    row_list_pos = row_mapping[r_heading]
    col_list_pos = col_mapping[c_heading]
    return row_list_pos, col_list_pos

# This function translates list positions to -> algebraic positions
# def get_alg_position(r_heading, c_heading):
def get_alg_positions(possible_moves):
    row_mapping = {8: 1, 7: 2, 6: 3, 5: 4, 4: 5, 3: 6, 2: 7, 1: 8 }
    col_mapping = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h' }
    user_possible_moves = []

    for id, move in enumerate(possible_moves):
        row = int(str(move)[0])
        col = int(str(move)[1])

        row_list_pos = row_mapping[row]
        col_list_pos = col_mapping[col]
        
        user_move = str(col_list_pos) + str(row_list_pos)
        user_possible_moves.append(user_move)
    return user_possible_moves

def get_piece_name(input_piece):
        switcher={
                "Q":"Queen",
                "R":"Rook",
                "K":"Knight"
             }
        return switcher.get(input_piece, "UnsupportedPiece")

def get_move_types(player_type):
    #print("LOOK, get_move_types got passed player_type of: " + get_piece_name(input_piece))
    switcher={
                "Q":("h","v")
                # BELOW IS CORRECT, PUT IT BACK LATER
                # "Q":("d","h","v")
                #"R":"Rook",
                #"K":"Knight"
             }
    move_types = switcher.get(player_type, "UnsupportedPlayer")
    return move_types


# def get_moves(move_type, board, row_position, col_position, move_types):
def get_moves(move_types, board, row_position, col_position):
    # move types (h horizontal, v vertical, d diagonal, l L-shaped)
    possible_moves = []

    # Iterate through move_types and print them out...
    for type in move_types: 
        # print("get_moves sees type of: " + type + " in move_types tuple...")
        # Horizontal
        if (type == "h"):
            for idx, col in enumerate(board[row_position]):
                if (idx > 0 and idx != col_position):
                    move = int(str(row_position) + str(idx))
                    possible_moves.append(move)
                    # Update the game board
                    board[row_position][idx] = "h"
        # Vertical
        if (type == "v"):
            for idx, row in enumerate(board):
                if (idx > 0 and idx != row_position):
                    move = int(str(idx) + str(col_position))
                    possible_moves.append(move)
                    # Update the game board
                    board[idx][col_position] = "v"

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

# Call get_list_position to return the outer and inner list locations (based on user input...)
row_position, col_position = get_list_position(input_position[1], input_position[0])
board[row_position][col_position] = input_piece

# given input_piece, determine what move types can be made:
move_types = get_move_types(input_piece)

# get possible moves the given piece can make based on provided board position:
possible_moves =  get_moves(move_types, board, row_position, col_position)

# Print game board
print_board(board)

print("possible_moves     : " + str(possible_moves))

# Get possible moves (in algebraic notation) to return to user 
user_possible_moves = get_alg_positions(possible_moves)

# Return list of possible moves to the user
for m in user_possible_moves[:-1]:
    print(m, end=', ')
print(user_possible_moves[-1])