"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""


import unittest

def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


class BSTIterator(object):  
    def __init__(self, root):
        self.ref = []
        self.loadHeight(root)

    def loadHeight(self, root):
        aux = root
        while aux:
            self.ref.append(aux)
            aux = aux.left    

    def hasNext(self):
        return (len(self.ref) > 0)
        
    def next(self):
        node = self.ref.pop()
        self.loadHeight(node.right)
        return node.val


class Test(unittest.TestCase):
    data = [
        ('[5,4,8,3,null,7,null,-1,null,6]', [-1, 3, 4, 5, 6, 7, 8])
    ]

    def test_bst_iterator(self):
        for (tree, result) in self.data:
            i, v = BSTIterator(deserialize(tree)), []
            while i.hasNext(): 
                v.append(i.next())

            print (v)
    

unittest.main()