class Stack:
    def __init__(self):
        self.data = list()
        self.minimum = list()

    def push(self, value):
        if (len(self.data) == 0):
            self.minimum.append(value)
        else:
            if(self.minimum[-1] >= value):
                self.minimum.append(value)
        self.data.append(value)
    
    def isEmpty(self):
        if len(self.data) == 0:
            return True
        return False
 
    def pop(self):

        if(len(self.data)) != 0:
            if (self.data[-1] == self.minimum[-1]):
                self.minimum.pop()
            return self.data.pop()
        else:
            print("Stack is empty, nothing to pop!")
    
    def peek(self):
        if(len(self.data)) != 0:
            return self.data[-1]
        else:
            print("Stack is empty, nothing to peek!")

    def min(self):
        return self.minimum[-1]
    
stack = Stack()
stack.pop()
stack.peek()
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(-3)
print(stack.min())
stack.pop()
print(stack.min())