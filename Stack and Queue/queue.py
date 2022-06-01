class Queue:
    def __init__(self):
        self.data = list()

    def add(self, value):
        self.data.append(value)
    
    def isEmpty(self):
        if len(self.data) == 0:
            return True
        return False
 
    def remove(self):
        if(len(self.data)) != 0:
            return self.data.pop(0)
        else:
            print("Queue is empty, nothing to remove!")
    
    def peek(self):
        if(len(self.data)) != 0:
            return self.data[0]
        else:
            print("Queue is empty, nothing to peek!")
    
    def getSize(self):
        return len(self.data)
    
# queue = Queue()
# print(queue.isEmpty())
# queue.add(0)
# queue.add(1)
# queue.add(2)
# queue.add(3)
# queue.add(4)
# print(queue.peek())
# print(queue.remove())
# print(queue.peek())
