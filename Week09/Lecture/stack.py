class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)
    
    def peek(self):
        #if len(self.stack) > 0:
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return None
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def pop(self):
        if self.isEmpty():
            return None
        lastElem = self.stack.pop()
        return lastElem
    
    def printStack(self):
        if self.isEmpty():
            print("Stack is empty!")
        else:
            print(self.stack)
