name = ["Joe", "Jack", "Robert", "Jacob", "Noah", "Milan", "Jesse", "Thomas"] #and etc until 20 names
Found = False
Student = input("Enter student name: ")
for index in range(0, len(name)):
    if name[index] == Student:
        print("Student ID is ", index + 1)
        Found = True
    #Endif
#Next n
if Found == False:
    print(Student, " was not found in the array!")
#endif
