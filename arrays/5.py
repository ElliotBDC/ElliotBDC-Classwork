Grid = [[], [], [], [], [], []] #Intialise array (list as python does not have arrays)
for n in range(0, 6):
    for x in range(0, 4):
        Grid[n].append("X")
    #Next x
#Next n
print(Grid)
Grid[0][0] = "O"
X = True
lastRow = 0
lastCol = 0
Row = int(input("Enter row value: "))
Column = int(input("Enter column value: "))
Grid[Row-1][Column-1] = "O"
Grid[lastRow][lastCol] = "X"
lastCol = Column-1
lastRow = Row-1
for n in range(0, 6):
    for x in range(0, 4):
        print(Grid[n][x], end="")
    #next n
    print("")
    #Print("\n") #Prints new row on the next line.
#Next n



