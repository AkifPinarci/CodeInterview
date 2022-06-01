import stack as check
# We hold the new elements in the stack new. When the old is empty, we reverse the new by popping all the new into the old. If the old is not empty, we directly work on the old.
class MyQueue:
    def __init__(self):
        self.new = check.Stack()
        self.old = check.Stack()
    
    def getSize(self):
        return self.old.size() + self.new.size()

    def push(self, value):
        self.new.push(value)


    def shiftStack(self):
        if(self.old.isEmpty()):
            while(not self.new.isEmpty()):
                self.old.push(self.new.pop())

    def peek(self):
        self.shiftStack()
        return self.old.peek()
    
    def pop(self):
        self.shiftStack()
        return self.old.pop()

queue = MyQueue()
queue.push(0)
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)
queue.push(6)
queue.push(7)
print(queue.peek())
queue.pop()
print(queue.peek())