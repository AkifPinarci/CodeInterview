class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


    def delete(self, val):
        head = self
        if head.val == val:
            head = head.next
            self = None
            self = head
            return self
        while(head.next is not None):
            if(head.next.val == val):
                head.next = head.next.next
                return self
            head = head.next
        return self
             
    def addToTail(self, val):
        end = Node(val)
        while(self.next is not None):
            self = self.next
        self.next = end


head = Node(0)

head.addToTail(1)
head.addToTail(2)
head.addToTail(3)
head.addToTail(4)

head.addToTail(5)
head.addToTail(6)
head.addToTail(7)
head.addToTail(8)
head.addToTail(9)
head.addToTail(10)
head.addToTail(11)
head.addToTail(12)
head.delete(1)
pointer = head
while(pointer.next != None):
    print(pointer.val)
    pointer = pointer.next
print(pointer.val)

