
mylist = [["8", "x", "x", "x", "x", "x", "x", "x", "x"],
["7", "x", "x", "x", "x", "x", "x", "x", "x"],
["6", "x", "x", "x", "x", "x", "x", "x", "x"],
["5", "x", "x", "x", "x", "x", "x", "x", "x"],
["4", "x", "x", "x", "x", "x", "x", "x", "x"],
["3", "x", "x", "x", "x", "x", "x", "x", "x"],
["2", "x", "x", "x", "x", "x", "x", "x", "x"],
["1", "x", "x", "x", "x", "x", "x", "x", "x"]]

# print("  a b c d e f g h")
for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        #if j >= 1:
            print(mylist[i][j], end = ' ')
        #else:
            #print(" " + mylist[i][j], end = ' ')
    print()


# mylist = [["x"] * 8 for i in range(8)]
# # print(mylist[1][2])
#for item in mylist:
#    print(str(item), end = '*')

# for x,y in mylist:
#    print(x,y)

#for i in mylist:
#    print(i[0], i[1])
# Printing list using map 
# print ("List in proper method", '[%s]' % ', '.join(map(str, mylist))) 

#print(mylist)
#for item in range(8):
#    print(chessBoard[i])    