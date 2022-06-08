import random as rn
class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = Tree(value)
        if value > self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = Tree(value)

    def inOrder(self, arr):
        arr.append(self)
        if self.left is not None:
            self.left.inOrder(arr)
        if self.right is not None:
            self.right.inOrder(arr)
        return arr

    def getRandom(self):
        possibilities = [0, 1, 2]
        choice = rn.choice(possibilities)
        if choice == 0:
            return self.value
        if choice == 1:
            if self.left is not None:
                return self.left.getRandom()
            else:
                return self.value
        if choice == 2:
            if self.right is not None:
                return self.right.getRandom()
            else:
                return self.value


root = Tree(9)
root.insert(7)
root.insert(6)
root.insert(8)
root.insert(56)
root.insert(75)
root.insert(54)
root.insert(33)
root.insert(73)
root.insert(10)

result = dict()
for i in range(100):
    value = root.getRandom()
    if value in result:
        result[value] += 1
    else:
        result[value] = 1

print(result)