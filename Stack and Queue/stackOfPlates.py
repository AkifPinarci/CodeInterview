class Stack:
    def __init__(self):
        self.data = [[]]
        self.limit = 7

    def push(self, value):
        if(len(self.data[-1])) < self.limit:
            self.data[-1].append(value)
        else:
            self.data.append([])
            self.data[-1].append(value)

    
    def isEmpty(self):
        if len(self.data[0]) == 0:
            return True
        return False
 
    def pop(self):
        if(len(self.data[-1]) == 1):
            self.data[-1].pop()
            self.data.pop()
        elif(len(self.data[-1])>1):
            self.data[-1].pop()
        else:
            print("Nothing to pop")
    
    def peek(self):
        if(len(self.data[-1])) != 0:
            return self.data[-1][-1]
        else:
            print("Stack is empty, nothing to peek!")
    
    def print(self):
        for i in range(0, len(self.data)):
            for k in self.data[i]:
                print(k, end=" ")
            print()
    
stack = Stack()
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
stack.push(9)
stack.push(10)
stack.push(11)
stack.print()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.print()
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
stack.push(9)
stack.push(130)
stack.push(11)
stack.print()