list1 = [2,5,15,36,47,56,59,78,156,244,268]
list2 = [18,39,42,43,66,69,100]
list3 = []
list1Counter = 0
for index in range(0, len(list2)):
    endLoop = False
    while endLoop == False:
            if list1Counter == len(list1):
                endLoop = True
                if list2[index] > list1[list1Counter-1]:
                    list3.append(list2[index])
            else:
                if list2[index] == list2[-1]:
                        if list1[list1Counter] < list2[index]:
                            list3.append(list1[list1Counter])
                            list1Counter = list1Counter + 1
                        elif list1[list1Counter] > list2[index]:
                            list3.append(list2[index])
                            for i in range(0, len(list1) - list1Counter):
                                list3.append(list1[list1Counter])
                                list1Counter = list1Counter + 1
                        else:
                            list3.append(list2[index])
                elif list1[list1Counter] < list2[index]:
                    list3.append(list1[list1Counter])
                    list1Counter = list1Counter + 1
                else:
                    list3.append(list2[index])
                    endLoop = True
print(list3)


