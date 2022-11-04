queue = []
size = 5
def enQueue(value):
    if isFull() == False:
        queue.append(value)
    else:
        return "Full"
    #endif

def deQueue(value=None):
    if value == None:
        queue.pop()
    else:
        queue.pop(queue.index(value))
        #endif

def isEmpty():
    if len(queue) != 0:
        return False
    #endif
    return True

def isFull():
    if len(queue) == 5:
        return True
    #endif
    return False

enQueue("Hello")
print(queue)
