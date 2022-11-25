myString = input("Enter word: ")
stack = []
s = ""
for c in myString:
    if 64 < ord(c) < 91:
        s = s + c
        stack.append(c)
    #end if
#next c

newString = ""
for _ in range(len(stack)):
    newString = newString + stack.pop()
#next _

if myString == newString:
    print("Palindrome")
else:
    print("Not Palindrome")
#end if

if myString == myString[::-1]:
    print("True")
#end if
