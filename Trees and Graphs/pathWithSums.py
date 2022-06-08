class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self,value):
        if value > self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = Tree(value)
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = Tree(value)

    def preOrder(self, arr):
        arr.append(self.value)
        if self.left is not None:
            self.left.preOrder(arr)
        if self.right is not None:
            self.right.preOrder(arr)
        return arr


root = Tree(20)
root.insert(19)
root.insert(30)
root.insert(11)
root.insert(5)
root.insert(7)
root.insert(3)

def sums(tree, target):
    if tree == None:
        return 0

    root = numPath(tree, target, 0)
    left = sums(tree.left, target)
    right = sums(tree.right, target)

    return root + left + right
    
def numPath(node, target, cur):
    if node == None:
        return 0
    cur += node.value
    total = 0
    if cur == target:
        total += 1
    total += numPath(node.left, target, cur)
    total += numPath(node.right, target, cur)
    return total

paths = sums(root, 50)
print(paths)