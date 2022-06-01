
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

    def partition(self, value):
        pointer = self.head
        while(pointer.next != None):
            if(pointer.value < value):
                val = pointer.value
                self.delete(pointer.value)
                self.addFront(val)
            pointer = pointer.next
        if(pointer.value < value):
            val = pointer.value
            self.delete(pointer.value)
            self.addFront(val)

    def reverse(self):
        pointer = self.head
        reversedList = LinkedList()
        while(pointer.next != None):
            reversedList.addFront(pointer.value)
            pointer = pointer.next
        reversedList.addFront(pointer.value)
        return reversedList

    def isPalindrome(self):
        reversedList = self.reverse()
        rev = reversedList.head
        pointer = self.head
        while(pointer.next != None):
            if (rev.value != pointer.value):
                return False
            else:
                pointer = pointer.next
                rev = rev.next        
        if (rev.value != pointer.value):
            return False
        return True