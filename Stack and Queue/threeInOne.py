class Stack:
    def __init__(self):
        self.data = [None] * 50
        self.numberOfStacks = 3
        self.index1 = 0
        self.index2 = 1
        self.index3 = 2

    def peek(self, number):
        if number == 1 and self.index1 != 0:
            return self.data[self.index1-3]

        elif number == 2 and self.index2 != 1:
            return self.data[self.index2-3]

        elif number == 3 and self.index3 != 2:
            return self.data[self.index3-3]


    def push(self, value, number):
        if number == 1:
            self.data[self.index1] = value
            self.index1 += 3
        elif number == 2:
            self.data[self.index2] = value
            self.index2 += 3
        elif number == 3:
            self.data[self.index3] = value
            self.index3 += 3

    def isEmpty(self, number):
        if number == 1 and self.index1 == 0:
            return True
        elif number == 2 and self.index2 == 1:
            return True
        elif number == 3 and self.index3 == 2:
            return True
        return False
        
    def pop(self, number):
        if number == 1:
            self.index1 -= 3
            result = self.data[self.index1]
            self.data[self.index1] = None
        elif number == 2:
            self.index2 -= 3
            result = self.data[self.index2]
            self.data[self.index2] = None
        elif number == 3:
            self.index3 -= 3
            result = self.data[self.index3]
            self.data[self.index3] = None
        return result
    
stack = Stack()

stack.push(1, 1)
stack.push(2, 1)
stack.push(3, 1)
stack.push(4, 1)
stack.push(44, 1)
stack.push(1, 2)
stack.push(2, 2)
stack.push(3, 2)
stack.push(4, 2)
stack.push(5, 2)
stack.push(55, 2)
stack.push(1, 3)
stack.push(2, 3)
stack.push(3, 3)
stack.push(4, 3)
stack.push(5, 3)
stack.push(6, 3)
stack.push(66, 3)

print(stack.peek(3))
print(stack.pop(3))
print(stack.peek(3))
print(stack.pop(3))
print(stack.pop(3))
print(stack.pop(3))
