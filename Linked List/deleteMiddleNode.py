class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addFront(self, value):
        new_value = Node(value)
        new_value.next = self.head
        self.head = new_value

    def print(self):
        pointer = self.head
        while pointer.next is not None:
            print(pointer.value)
            pointer = pointer.next
        print(pointer.value)

    def addEnd(self, value):
        new_value = Node(value)
        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next
        pointer.next = new_value
    
    def delete(self, key):
         
        # Store head node
        temp = self.head
 
        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.value == key):
                self.head = temp.next
                temp = None
                return
 
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.value == key:
                break
            prev = temp
            temp = temp.next
 
        # if key was not present in linked list
        if(temp == None):
            return
 
        # Unlink the node from linked list
        prev.next = temp.next
 
        temp = None

    def getLength(self):
        length = 0
        pointer = self.head
        while pointer.next is not None:
            length += 1
            pointer = pointer.next
        return length + 1

    def removeDups(self):
        pointer = self.head
        prev = None
        dups = dict()

        while pointer != None:
            if pointer.value not in dups:
                dups[pointer.value] = 1
                prev = pointer
            else:
                prev.next = pointer.next
            pointer = pointer.next

    # Learn it by recursion and wiht other techniques.
    def kThLastElementh(self, index):
        pointer = self.head
        length = self.getLength()
        target = length - index
        while target > 0:
            pointer = pointer.next
            target -= 1


        print("The Kth to Last Elementh:",pointer.value)
        return pointer.value

    def deleteMiddle(self):
        return 0


linkedList = LinkedList()
linkedList.addFront(0)
linkedList.addEnd(1)
linkedList.addEnd(2)
linkedList.addEnd(3)
linkedList.addEnd(4)
linkedList.addEnd(5)
linkedList.addEnd(6)
linkedList.addEnd(7)
linkedList.addEnd(8)
linkedList.addEnd(9)
linkedList.print()
length = linkedList.getLength()
middle = length // 2
linkedList.delete(linkedList.kThLastElementh(middle+1))
linkedList.print()