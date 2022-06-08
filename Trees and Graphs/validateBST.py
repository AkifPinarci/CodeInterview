class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Tree(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Tree(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def postOrderTraversal(self):
        if self.left:
            self.left.postOrderTraversal()
        if self.right:
            self.right.postOrderTraversal()
        print(self.value)

tree = Tree(20)
tree.insert(10)
tree.insert(30)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.postOrderTraversal()