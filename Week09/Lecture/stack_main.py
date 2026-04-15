from stack import Stack
from collections import deque

def checkExpression_v2(exp):
    myStack = deque()
    d = {
        "]": "[",
        ")": "(",
        "}": "{"
    }

    # d["]"] -> returns "["
    for ch in exp:
        # chech whether ch is an opening bracket
        if ch in d.values():
            myStack.append(ch)
        else:
            if not myStack:
                return False
            # check peek value is same with expected opening version
            if myStack[-1] == d[ch]:
                myStack.pop()
            else:
                return False
    
    if not myStack:
        return True
    return False

def checkExpression(exp):
    myStack = Stack()
    d = {
        "]": "[",
        ")": "(",
        "}": "{"
    }

    # d["]"] -> returns "["
    for ch in exp:
        # chech whether ch is an opening bracket
        if ch in d.values():
            myStack.push(ch)
        else:
            if myStack.isEmpty():
                return False
            # check peek value is same with expected opening version
            if myStack.peek() == d[ch]:
                myStack.pop()
            else:
                return False
    
    if myStack.isEmpty():
        return True
    return False



"""
myStack = Stack()
myStack.printStack()
myStack.push(10)
myStack.push(20)
myStack.push(30)
lastElem = myStack.peek()
print(lastElem)
myStack.printStack()
lastElem = myStack.pop()
print(lastElem)
myStack.printStack()
"""

print(checkExpression_v2("()[]{}"))
print(checkExpression_v2("(([]))[]{}"))
print(checkExpression_v2("(([]))[[]{}"))
print(checkExpression_v2("(([]))[([{[[[()]]]}])]{}"))