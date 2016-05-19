"""
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth 
if you have a tree of depth D, you'll have D linked list
"""
from collections import deque

class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class ListNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.root = None

    def add(self, value):
        node = ListNode(value)
        if self.root is None:
            self.root = node
        else:
            aux = self.root
            while aux.next:
                aux = aux.next
            aux.next = node
    def show(self):
        aux = self.root
        print ('List:')
        while aux:
            print (aux.val, end=', ')
            aux = aux.next
        print ()
            

class DepthLists(object):
    
    def __init__(self, tree):
        self.root = tree
        self.lists = []
        self.traverse()

    def traverse(self):
        depth = 0
        queue = deque( [(self.root, depth)] )

        while len(queue) > 0:           
            node, depth = queue.popleft()
            if node is not None:
                self.addToList(depth, node.val)
                if node.left is not None:
                    queue.append( (node.left, depth + 1) )
                if node.right is not None:
                    queue.append( (node.right, depth + 1) )

    def addToList(self, depth, value):      
        if depth > 0:
            if depth > len(self.lists):
                llist = LinkedList()
                self.lists.append(llist)
            self.lists[depth - 1].add(value)

    def getList(self):
        return self.lists



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

solution = DepthLists(root)
lists = solution.getList()
for l in lists: 
    l.show()