### SRC - This is a great effort, I've made some cooments below for you to look at.
#Test1: 2 Candidates A has majority

test1 = ['B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 
'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 
'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 
'A', 'A', 'A', 'B', 'B', 'A', 'B']

#Test2: 2 Candidates No majority

test2 = ['B', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 
'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 
'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 
'A', 'B', 'A', 'B', 'A', 'B', 'B']

#Test3: 2 Candidates B has majority

test3 = ['B', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 
'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 
'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'A', 'A',
'B', 'B', 'B', 'A', 'A', 'B', 'A']

#Test4: 4 Candidates A has majority

test4 = ['A', 'A', 'C', 'B', 'A', 'B', 'D', 'D', 'C', 'A', 'A', 'A', 'A', 'C', 'C', 'A', 'A', 'D', 'A', 'D', 'A', 'A', 'A', 'C', 'C', 'A', 'D', 'A', 'A', 'A', 'A', 
'C', 'B', 'C', 'D', 'C', 'C', 'C', 'A', 'C', 'D', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'C', 'A', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'D', 'A', 'C', 'D', 'C', 
'A', 'A', 'D', 'A', 'B', 'C', 'A', 'A', 'B', 'B', 'D', 'A', 'B', 'A', 'D', 'D', 'A', 'A', 'A', 'C', 'D', 'A', 'A', 'C', 'A', 'A', 'D', 'A', 'A', 'A', 'A', 
'A', 'A', 'B', 'A', 'D', 'C', 'C']

#Test5: 4 Candidates No majority

test5 = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'C', 'C', 'B', 'B', 'C', 'C', 'C', 'D', 'C', 'C', 
'D', 'C', 'B', 'C', 'B', 'B', 'B', 'B', 'D', 'D', 'D', 'C', 'D', 'D', 'C', 'C', 'B', 'C', 'D', 'D', 'C', 'C', 'C', 'C', 'C', 'D', 'C', 'C', 'C', 'B', 'D', 
'C', 'C', 'C', 'B', 'C', 'D', 'C', 'D', 'C', 'C', 'D', 'D', 'C', 'C', 'C', 'B', 'B', 'B', 'B', 'B', 'C', 'D', 'C', 'D', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 
'D', 'B', 'B', 'D', 'D', 'D', 'D']

#1: Add the top of stack_mix to stack 2
#2: If the top of stack 2 is the same as the top of stack mix, add the top of stack mix to stack2, else add both of them to stack 3
#3: Repeat step 2 (if stack_mix is empty, always add to stack 2).
#4: Once stack_mix is empty, if there is any letters left in stack 2, that letter may have the majority, if there are no letters in 
# the stack 2, there is no majority.
#5: If there may be a majority, add stack 2 to stack 3 and repeat the process from #1, and if again, there is the same letter in
# stack 2, then there is certainly a majority. 

def solve_majority(aStack):
    stack_two = []
    stack_three = []
    first_pass(aStack, stack_two, stack_three)
    second_pass(stack_three, stack_two, aStack)
    return stack_two
    ### SRC - You should try and avoid repeating code. Try using two functions here,
    ### one to carry out the algorithm, with three stacks as parameters, and one driving
    ### function to repeat the first function again with different arguments (if necessary)

def first_pass(stack_mix, stack_two, stack_three):
    while len(stack_mix) != 0:
        ### SRC - No need for a variable here...
        if len(stack_two) == 0 or stack_two[-1] == stack_mix[-1]:
            stack_two.append(stack_mix.pop())
        else:
            ### SRC - or here
            stack_three.append(stack_two.pop())
            stack_three.append(stack_mix.pop())
    return stack_two

def second_pass(stack_three, stack_two, stack_mix):
    if len(stack_two) == 0:
        return
    first_pass(stack_three, stack_two, stack_mix)
    return

if solve_majority(test1)[0] == "A":
    print("✓ Test 1 Passed")
else:
    print("#### Test 1 failed")    

if len(solve_majority(test2)) == 0:
    print("✓ Test 2 Passed")
else:
    print("#### Test 2 failed")    

if solve_majority(test3)[0] == "B":
    print("✓ Test 3 Passed")
else:
    print("#### Test 3 failed")    

if solve_majority(test4)[0] == "A":
    print("✓ Test 4 Passed")
else:
    print("#### Test 4 failed")    

if len(solve_majority(test5)) == 0:
    print("✓ Test 5 Passed")
else:
    print("#### Test 5 failed")   
