class LinkedList:
    listNodes = [None]
    def __init__(self):
        self.nextFree = 0
        self.start = None

    def __repr__(self) -> str:
        return f'{self.listNodes}'

    def add(self, name):
        if self.start != None:
            try:
                self.listNodes[self.nextFree] = Node(name, None)
            except:
                self.listNodes.append(Node(name, None))
            self.findNewPos(self.listNodes[self.nextFree])
            self.nextFree = self.findNextFree()
        if self.start is None:
            self.listNodes[self.nextFree] = (Node(name, -1)) #Pointer None means its the end of the list
            self.start = 0
            self.nextFree = 1

    def findNextFree(self):
        for i in range(0, len(self.listNodes)):
            if self.listNodes[i] is None:
                self.nextFree = i
                break
            elif i == len(self.listNodes)-1:
                self.nextFree = i+1
        return self.nextFree

    def findNewPos(self, newNode):
        for pointer in range(0, len((self.listNodes))):
            for i in range(0, len(self.listNodes)):
                if self.listNodes[i].pointer == self.listNodes.index(self.listNodes[pointer]):
                    break
            if self.listNodes[pointer].pointer == -1:
                if self.listNodes[pointer].name < newNode.name:
                    newNode.pointer = -1
                    #self.listNodes[pointer].pointer = self.listNodes.index(newNode)
                    self.listNodes[pointer].setParent(newNode, self.listNodes.index(newNode))
                    break

            if pointer == 0:
                node = self.listNodes[self.start]

                if self.listNodes[self.start].name > newNode.name:
                    self.start = self.listNodes.index(newNode)
                    newNode.setParent(node, self.listNodes.index(node))
                    break

            elif self.listNodes[pointer].name > newNode.name > self.listNodes[i].name:
                newNode.setParent(self.listNodes[pointer], self.listNodes.index(self.listNodes[pointer]))
                #for i in range(0, len(self.listNodes)):
                #    if self.listNodes[i].pointer == self.listNodes.index(self.listNodes[pointer]):
                #        break
                self.listNodes[i].setParent(newNode, self.listNodes.index(newNode))
                break

    def remove(self, name):
        for index in range(0, len(self.listNodes)):
            if self.listNodes[index].name == name:
                for i in range(0, len(self.listNodes)):
                    if self.listNodes[i].pointer == index:
                        break
                self.listNodes[i].setParent(self.listNodes[index].getParent() ,self.listNodes[index].pointer)

    def printAlphabetically(self):
        newNode = self.listNodes[self.start]
        print(newNode)
        for index in range(0, len(self.listNodes)-1):
            newNode = newNode.getParent()
            if newNode.getParent() == False:
                print(newNode)
                break
            print(newNode)

    def reverse(self):
        ...
class Node:
    parent = None
    def __init__(self, name, pointer):
        self.name = name
        self.pointer = pointer

    def __repr__(self) -> str:
        return f'( {self.name} --> {self.pointer} )'

    # def setPointer(self, pointer):
    #   self.pointer = pointer

    def getPointer(self):
        return self.pointer

    def getParent(self):
        if self.parent is None:
            return False
        return self.parent

    def setParent(self, parentNode, index):
        self.parent = parentNode
        self.pointer = index


newLinked = LinkedList()
newLinked.add("Amy")
newLinked.add("April")
newLinked.add("Haider")
newLinked.add("Otto")
newLinked.add("Salman")
newLinked.add("Oliver")

newLinked.remove("Haider")  # Haider is not deleted from the linked list, however he is skipped.

print(f"NextFree: {newLinked.nextFree}, Start: {newLinked.start}")
print("-------|----------|---------")
print("Index  --  Name  --  Pointer")
print("-------|----------|---------")
for i in range(0, len(newLinked.listNodes)):
    freespace = 6 - len(newLinked.listNodes[i].name)
    print(str(i) + "    --    " + newLinked.listNodes[i].name + " " * freespace + "    --    " + str(newLinked.listNodes[i].pointer))

print(" ")
newLinked.printAlphabetically()

