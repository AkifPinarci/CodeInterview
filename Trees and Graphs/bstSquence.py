class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value > self.value and self.right != None:
            self.right.insert(value)
        if value < self.value and self.left != None:
            self.left.insert(value)

        if value > self.value and self.right ==None:
            self.right = Tree(value)
        elif value < self.value and self.left == None:
            self.left = Tree(value)

    def postOrderTraversal(self):
        if self.left:
            self.left.postOrderTraversal()
        if self.right:
            self.right.postOrderTraversal()

    def getHeight(self):
        return 0

def getLevelOrder(tree):
    levelOrder = dict()
    def dfs(node, depth):
        if node.left != None:
            dfs(node.left, depth+1)
        if node.right != None:
            dfs(node.right, depth+1)
        if depth not in levelOrder:
            levelOrder[depth] = [node.value]
        else:
            levelOrder[depth].append(node.value) 
    dfs(tree, 0)
    return levelOrder

def n_length_combo(lst, n):
     
    if n == 0:
        return [[]]
    l =[]
    for i in range(0, len(lst)):
         
        m = lst[i]
        remLst = lst[0:i] + lst[i + 1:]
         
        remainlst_combo = n_length_combo(remLst, n-1)
        for p in remainlst_combo:
            l.append([m, *p])
           
    return l

def get_array(comb):
    result = []
    for i in range(len(comb)):
        for j in comb[i][0]:
            result.append(j)
    return(result)


tree = Tree(20)
tree.insert(10)
tree.insert(30)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.postOrderTraversal()
liste = getLevelOrder(tree)
for i in liste:
    liste[i] = n_length_combo(liste[i], len(liste[i]))
print(get_array(liste))

