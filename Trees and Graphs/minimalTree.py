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

def arrayToBST(arr):
    if len(arr) == 0:
        return None

    mid = len(arr) // 2
    root = Tree(arr[mid])
    root.left = arrayToBST(arr[:mid])
    root.right = arrayToBST(arr[mid+1:])
    return root
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

root = arrayToBST(array)
