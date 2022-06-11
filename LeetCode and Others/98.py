class Tree:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


node1 = Tree(1)
node1.right = Tree(1)




def isValidBST(root):
    
    def dfs(node, left, right):
        if node is None:
            return True
        if not (node.val < right and node.val > left):
            return False
        return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

    dfs(root, float("-inf"), float("inf"))
print(isValidBST(node1))