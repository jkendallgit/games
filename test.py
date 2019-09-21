# Initialize chess board

mylist = [[" ", "  a", "   b", "   c", "   d", "   e", "   f", "   g", "   h"],
["8", " ", " ", " ", " ", " ", " ", " ", " "],
["7", " ", " ", " ", " ", " ", " ", " ", " "],
["6", " ", " ", " ", " ", " ", " ", " ", " "],
["5", " ", " ", " ", " ", " ", " ", " ", " "],
["4", " ", " ", " ", " ", " ", " ", " ", " "],
["3", " ", " ", " ", " ", " ", " ", " ", " "],
["2", " ", " ", " ", " ", " ", " ", " ", " "],
["1", " ", " ", " ", " ", " ", " ", " ", " "]]

# Draw Chess Board (this needs to turn into a function)
for i in range(len(mylist)):
    if i > 0:
        print("   ---  ---  ---  ---  ---  ---  ---  ---")
    for j in range(len(mylist[i])):
        if i > 0 and j > 0:
            print(" |" + mylist[i][j] + "|", end = ' ')
        else:
            print(mylist[i][j], end = ' ')
    print()