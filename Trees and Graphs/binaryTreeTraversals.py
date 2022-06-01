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

    def inOrderTraversal(self):
        if self.left:
            self.left.inOrderTraversal()
        print(self.value)
        if self.right:
            self.right.inOrderTraversal()

    def postOrderTraversal(self):
        if self.left:
            self.left.postOrderTraversal()
        if self.right:
            self.right.postOrderTraversal()
        print(self.value)

    def preOrderTraversal(self):
        print(self.value)
        if self.left:
            self.left.preOrderTraversal()
        if self.right:
            self.right.preOrderTraversal()

def main():

    binaryTree = Tree(4)
    binaryTree.insert(2)
    binaryTree.insert(1)
    binaryTree.insert(3)
    binaryTree.insert(5)
    binaryTree.insert(6)
    binaryTree.preOrderTraversal()
    
if __name__ == "__main__":
    main()