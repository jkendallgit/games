def print_board(board):
    for i in range(len(board)):
        print(" --------------------------------------")
        for j in range(len(board[i])):
            print(" |" + board[i][j] + "|", end = ' ')
        print()

board = [[ " " , " " , " " , " " , " " , " " , " " , " "] for i in range(8)]
board[4][4] = "X"
print_board(board)
# next write some code to print out possible diagonal moves for X...

#for i, item in enumerate(board[2:], start=1):
#    print(item)

# print(str(board[2:][-4:]))

#mylist = []
#mylist.append("asdf")
#mylist.append("jkl;")

#mylist = ["41", "42", "44", "45", "46", "47", "48"]
#print(mylist)
#for idx, rp in enumerate(mylist):
#    print(mylist[idx][0])
#    print(mylist[idx][1])


#if (current_row < last_row and current_col < last_col):
#    next_cell = [current_row + 1][current_col + 1]
#    v_moves = v_moves + next_cell 

