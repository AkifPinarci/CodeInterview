class MinHeap:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.size = 0


    def getParentIndex(self, index):
        return (index - 1) // 2
    
    def getLeftChildIndex(self, index):
        return 2 * index + 1

    def getRightChildIndex(self, index):
        return 2 * index + 2
    
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) <self.size

    def parent(self, index):
        return self.storage[self.getParentIndex(index)]

    def leftChild(self, index):
        return self.storage[self.getLeftChildIndex(index)]

    def rightChild(self, index):
        return self.storage[self.getRightChildIndex(index)]

    def isFull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]

    def insert(self, data):
        if self.isFull():
            raise ("Heap is full!") 
        else:
            self.storage[self.size] = data
            self.size += 1
            self.heapifyUp(self.size - 1)
    
    def heapifyUp(self, index):
        if(self.hasParent(index) and self.parent(index) > self.storage[index]):
            self.swap(self.getParentIndex(index), index)
            self.heapifyUp(self.getParentIndex(index))

    def removeMin(self):
        if self.size == 0:
            raise ("Heap is empty!")
        else:
            data = self.storage[0]
            self.storage[0] = self.storage[self.size - 1]
            self.size -= 1
            self.heapifyDown(0)
            return data
        
    def heapifyDown(self, index):
        smallest = index
        if(self.hasLeftChild(index) and self.storage[index] > self.leftChild(index)):
            smallest = self.getLeftChildIndex(index)
        if(self.hasRightChild(index) and self.storage[smallest] > self.rightChild(index)):
            smallest = self.getRightChildIndex(index)
        if(smallest != index):
            self.swap(index, smallest)
            self.heapifyDown(smallest)

        # Iterative method, modify function call in removeMin to use iterative method.
        # index = 0
        # while(self.hasLeftChild(index)):
        #     smaller = self.getLeftChildIndex(index)
        #     if(self.hasRightChild(index) and self.leftChild(index) > self.rightChild(index)):
        #         smaller = self.getRightChildIndex(index)
        #     if(self.storage[index] > self.storage[smaller]):
        #         self.swap(index, smaller)
        #     else:
        #         break
        #     index = smaller

    def printHeap(self):
        print(self.storage)

heap = MinHeap(20)
heap.insert(2)
heap.insert(1)
heap.insert(6)
heap.insert(9)
heap.insert(7)
heap.insert(3)
heap.insert(5)
heap.insert(15)
heap.insert(25)
heap.insert(45)
heap.insert(35)
heap.insert(4)
heap.removeMin()
heap.printHeap()
