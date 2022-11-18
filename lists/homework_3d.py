records = ["Banana", "Strawberry", "Melon", "Lemon"]
endLoop = True
pointers = []
start = 0
pointers = [3, -1, 1, 2]
pointer = start
while endLoop == True:
    if pointer != -1:
        print(records[pointer])
        pointer = pointers[pointer]
    else:
        endLoop = False


