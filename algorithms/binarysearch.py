list1 = [1, 2, 3, 4, 4.5, 4.7, 5, 7, 8, 9]
left_pointer = 0
right_pointer = len(list1) - 1
found = False
target = 10
while found == False:
    m = left_pointer + (right_pointer-left_pointer) // 2
    print(m)
    if list1[m] != target and left_pointer == right_pointer:
        print("Not in array")
        found = True
    elif list1[m] == target:
        print(f"{target} was found at index {m}")
        found = True
    elif target > list1[m]:
        left_pointer = left_pointer + 1
    elif target < list1[m]:
        right_pointer = right_pointer - 1


