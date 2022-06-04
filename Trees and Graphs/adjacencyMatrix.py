class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.state = False


class Graph:
    def __init__(self):
        self.nodes = []

def searchBFS(start, end):
    if start == end:
        return True
    
    visited = set()
    queue = []
    queue.append(start)
    while len(queue) > 0:
        u = queue.pop(0)
        for k in u.children:
            if k == end:
                return True
            else:
                if k not in visited:
                    queue.append(k)
                    visited.add(k)

    return False

node0 = Node("Node0")
node1 = Node("Node1")
node2 = Node("Node2")
node3 = Node("Node3")
node4 = Node("Node4")
node5 = Node("Node5")
node0.children = [node1, node4, node5]
node1.children = [node3, node4]
node2.children = [node1]
node3.children = [node2, node4]
node4.children = []
node5.children = []



print(searchBFS(node0, node5))