def printAlphabetically(self):
        newNode = self.listNodes[self.start]
        for index in range(0, len(self.listNodes)-1):
            print(newNode)
            newNode = self.listNodes[newNode.pointer]
