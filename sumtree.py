class SumTree:
    def __init__(self):
        self.root = None


class Node:
    def __init__(self):
        self.key = 0
        self.parent = None
        self.left = None
        self.right = None


def makeNode(key):
    n = Node()
    n.key = key
    return n


def buildSumTree(array):
    for i in range(len(array)):
        array[i] = makeNode(array[i])
    tree = SumTree()
    tree.root = buildSumTree_rec(array)
    return tree


def buildSumTree_rec(array):
    if len(array) == 1:
        return array[0]
    else:
        a = []
        for i in range(0, len(array) // 2, 2): 
            n = makeNode(array[i].key + array[i + 1].key)
            n.left = array[i]
            n.right = array[i + 1]
            array[i].parent = n
            a.append(n)
        return buildSumTree_rec(a)
