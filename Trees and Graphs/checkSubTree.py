class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preOrder(node, arr):
    if node == None:
        arr.append("X")
        return
    arr.append(node.value)  

    preOrder(node.left, arr)

    preOrder(node.right, arr)

node1 = Tree(1)
node2 = Tree(2)
node3 = Tree(3)
node4 = Tree(4)

node1.left = node2
node1.right = node3
node2.left = node4
node3.right = Tree(5)

node13 = Tree(3)
node13.right = Tree(5)

def checkSub(root1, root2):
    arr1 = list()
    arr2 = list()
    preOrder(root1, arr1)
    preOrder(root2, arr2)
    print(arr1)
    print(arr2)
    for i in range(len(arr1)):
        if arr1[i:] == arr2:
            return True
    return False

print(checkSub(node1, node13))
