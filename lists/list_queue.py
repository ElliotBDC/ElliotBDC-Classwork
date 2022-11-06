### SRC - A good attempt, but you needed to return the popped value
### and you need to make sure you identify your functions and procedures
### in the pseudocode comments. I would expect you to have more test cases 
### to show this is working correctly.

queue = []
size = 5
def enQueue(value):
    if isFull() == False:
        queue.append(value)
    else:
        return "Full"
    #endif
#end procedure

def deQueue(value=None):
    if value == None:
        queue.pop() ### You need to retuen the popped value
    else:
        queue.pop(queue.index(value))
    #endif
#end function
    

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
