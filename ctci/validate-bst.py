"""
Implement a function to check if a binary tree is a binary search tree
"""

import sys


class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def checkBinary(node):
	if node:
		if not checkBinary(node.left) or not checkBinary(node.right):
			return False

		vleft = -sys.maxsize
		vright = sys.maxsize

		if node.left: vleft = node.left.val
		if node.right: vright = node.right.val
			
		if 	vleft <= node.val and node.val < vright:
			return True
		else:
			return False
	return True
	

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)

sol = checkBinary(root)
print (sol)




