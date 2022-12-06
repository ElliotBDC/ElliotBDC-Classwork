num_list = [6, 5, 4, 3, 2, 1]
n = len(num_list)
for i in range(0, len(num_list)-1):
    for j in range(0, n-i-1):
        if num_list[j] > num_list[j+1]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
        
print(num_list)
