num_list = [1, 2, 3, 4, 5, 6]
n = len(num_list)
for i in range(0, len(num_list)-1):
    swaps = 0
    for j in range(0, n-i-1):
        if num_list[j] > num_list[j+1]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
            swaps = swaps + 1
    if swaps == 0:
        break
print(num_list)
