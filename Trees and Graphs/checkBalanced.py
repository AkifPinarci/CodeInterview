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
array = [1, 2, 3, 4, 5, 6, 7]

root = arrayToBST(array)

def in_order_traversal(tree):
    elements = []
    def dfs(node, depth):
        if node.left != None:
            dfs(node.left, depth + 1)
        elements.append(node.value)
        if node.right != None:
            dfs(node.right, depth + 1)
    dfs(tree, 0)
    return elements

result = in_order_traversal(root)
def check_order(array):
    for i in range(len(array) - 1):
        if(array[i] > array[i+1]):
            return False
    return True

print(check_order(result))