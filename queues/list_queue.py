### SRC - A good attempt, but you needed to return the popped value
### and you need to make sure you identify your functions and procedures
### in the pseudocode comments. I would expect you to have more test cases 
### to show this is working correctly. #CORRECTED

queue = []
size = 5
def enQueue(value):
    if isFull() == False:
        queue.append(value)
    else:
        return "Full"
    #endif
#end function

def deQueue(value=None):
    if value == None:
        return_value = queue.pop(0) ### You need to retuen the popped value <-- FIXED
    else:
        return_value = queue.pop(queue.index(value))
    return return_value
    #endif
#end function


def isEmpty():
    if len(queue) != 0:
        return False
    #endif
    return True
#end function <-- Added after fix

def isFull():
    if len(queue) == 5:
        return True
    #endif
    return False
#end function 

#New test cases added, to ensure the queue works

enQueue("Hello")
print(queue)
enQueue("Elliot")
print(deQueue())
print(deQueue("Elliot"))
print(f"Queue Full: {isFull()}, Queue Empty: {isEmpty()}, Queue Size: {len(queue)}")
print(queue)
