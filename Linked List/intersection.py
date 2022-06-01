
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

def addLists(list1, list2):
    result = LinkedList()
    number1 = 0
    number2 = 0
    power= 0
    pointer1 = list1.head
    pointer2 = list2.head
    while pointer1.next != None:
        number1 += (pointer1.value * (10**power))
        pointer1 = pointer1.next
        power += 1
    number1 += (pointer1.value * (10**power))
    pointer1 = pointer1.next
    power = 0
    while pointer2.next != None:
        number2 += (pointer2.value * (10**power))
        pointer2 = pointer2.next
        power += 1
    number2 += (pointer2.value * (10**power))
    pointer2 = pointer2.next
    power = 0

    # If the order does not need to be reversed
    # lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295. 
    # number1 = int(str(number1)[::-1])
    # number1 += int(str(number2)[::-1])
    # number1 = str(number1)
    # for i in number1:
    #     if(result.head == None):
    #         result.addFront(int(i))
    #     else:
    #         result.addEnd(int(i))


    # If the order needs to be reversed
    # Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295. 
    number1 += number2
    number1 = str(number1)
    for i in number1[::-1]:
        if(result.head == None):
            result.addFront(int(i))
        else:
            result.addEnd(int(i))
    return result



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
# output = addLists(linkedList, linkedList)
