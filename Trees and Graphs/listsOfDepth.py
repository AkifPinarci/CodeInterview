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
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

root = arrayToBST(array)


def nodesAtEachDepthBFS(tree):
    result = []
    current = []
    if tree.value != None:
        current.append(tree)
    while len(current) > 0:
        result.append(current)
        parents = current
        current = []
        for i in parents:
            if i.left != None:
                current.append(i.left)
            if i.right != None:
                current.append(i.right)
    return result

def nodesAtEachDepthDFS(tree):
    result = dict()
    visited = set()
    def dfs(node, depth):
        if node not in visited:
            if depth in result:
                result[depth].append(node.value)
            else:
                result[depth] = [node.value]
        visited.add(node)
        if node.left != None:
            dfs(node.left, depth+1)
        if node.right != None:
            dfs(node.right, depth+1)
    dfs(tree, 0)
    return result

resultDFS = (nodesAtEachDepthDFS(root))
print(resultDFS)
resultBFS = (nodesAtEachDepthBFS(root))

for i in resultBFS:
    for j in i:
        print(j.value, end=' ')
    print()
