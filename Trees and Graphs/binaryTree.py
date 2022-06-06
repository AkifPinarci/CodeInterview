from tkinter import N


class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def in_order(tree):
    if(tree.left != None):
        in_order(tree.left)
    print(tree.value)
    if(tree.right != None):
        in_order(tree.right)

def is_child(parent, child):
    check = [False]
    def dfs(node, depth):
        if node.left != None:
            dfs(node.left,depth+1)
        if node.right != None:
            dfs(node.right,depth+1)
        if node == child:
            check[0] = True
    dfs(parent, 0)
    return check[0]

def res(tree, node1, node2):
    g = [None]
    def post_order(tree, node1, node2):
        if(tree.left != None):
            post_order(tree.left, node1, node2)
        if(tree.right != None):
            post_order(tree.right, node1, node2)
        if(is_child(tree, node1) and is_child(tree, node2)):
            if g[0] == None:
                g[0] = tree.value
    post_order(tree, node1, node2)
    return g[0] 
def main():
    root = Tree(20)
    node10 = Tree(10)
    node30 = Tree(30)
    node5 = Tree(5)
    node3 = Tree(3)
    node7 = Tree(7)
    node15 = Tree(15)
    node17 = Tree(17)
    root.left = node10
    root.right = node30
    node10.left = node5
    node10.right = node15
    node15.right = node17
    node5.right = node7
    node5.left = node3
    node3.left = Tree(99)
    node30.left = Tree(993)
    node30.right = Tree(87)
    node30.left.left = Tree(-3)
    node30.left.right = Tree(66)
    node30.right.left = Tree(8)
    node30.right.right = Tree(4)
    print(res(root, node30.right.left, node30.right.right))

if __name__ == "__main__":
    main()