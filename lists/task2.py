### SRC - okay, but there were some issues with 
### invalid charcters (the result of pasting from word)
### and problems with indentation. Make sure this is all working
### in future.

list1 = [34,56,34,26,80,57,98,100,80,64,102,300,35,6,87,88]
count = 0
for index in range(0, len(list1)):
	if (list1[index] >=80) and (list1[index] <=100):
		count = count + 1
	#endif
#next index
print("Number of integers in range 80-100", count)

list2 = []
for index in range(0, len(list1)):
	if (list1[index] >=80) and (list1[index] <=100):
		item = list1[index]
		list2.append(item)
	#endif
#next index
print("New list containing values between 80 and 100: " + str(list2)) #Fix<-- can only concatenate str + str, therefore had to convert list2 to a str using str()
