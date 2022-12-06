gnames = ["Amelia","Olivia","Isla","Emily","Poppy", "Ava","Isabella","Jessica","Lily","Sophie"]

def linearSearch(list, name):
        i = 0
        while i < len(list):
            if list[i] == name:
                return i
            #end if
            i = i + 1
        return -1
    #end function

print(linearSearch(gnames, "Lily"))
print(linearSearch(gnames, "Amy"))
