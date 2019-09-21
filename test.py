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

# -piece KNIGHT -position d2
mylist[7][4] = "K" #d2

# Next step, given an input coordinate like "d2", Draw a "K" as an item at that location within the list matrix.
#d2
print(mylist[7][4])
8 => 1
7 => 2

#Do mappingin 2 steps, 2nd param passed in, like "2" will map to the "7th item in first (row) list,
# and then the 1st param that got passed in, like "d" will map to the 4th item in second (col) list.



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