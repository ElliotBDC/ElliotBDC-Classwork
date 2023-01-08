Park = [[],[],[],[],[],[],[],[],[],[]] #Initialising Park as a 6 by 10 array (but as a list)
for i in range(0, 10):
    for x in range(0, 6):
        Park[i].append("empty")
    #next x
#next i
x = True
registration = input("Enter registration: ")
column = int(input("Enter column: "))
row = int(input("Enter row: "))
if Park[row-1][column-1] == "empty" and 0 < row <11 and 0 < column < 7:
    Park[row-1][column-1] = registration
else:
    print("That space is taken / No such space exists")
for n in range(0, 10):
    for x in range(0, 6):
        print(f" | {Park[n][x]} |" , end="")
    #next n
    print("")
#next n
