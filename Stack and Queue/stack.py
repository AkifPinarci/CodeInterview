class Stack:
    def __init__(self):
        self.data = list()

    def push(self, value):
        self.data.append(value)
    
    def isEmpty(self):
        if len(self.data) == 0:
            return True
        return False
 
    def pop(self):
        if(len(self.data)) != 0:
            return self.data.pop()
        else:
            print("Stack is empty, nothing to pop!")
    
    def peek(self):
        if(len(self.data)) != 0:
            return self.data[-1]
        else:
            print("Stack is empty, nothing to peek!")
    
stack = Stack()
print(stack.isEmpty())
stack.pop()
stack.peek()
stack.push(0)
stack.push(1)
stack.push(2)
print(stack.isEmpty())
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.pop())
print(stack.pop())
print(stack.peek())
print(stack.pop())

