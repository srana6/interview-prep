"""
Invert a binary tree.
"""



class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def invertTree(self, root):
		if root:
			root.left, root.right = root.right, root.left
			self.invertTree(root.left)
			self.invertTree(root.right)
		return root
		
	def printTree(self, root):
		if not root:
			return None
		print (root.val)
		self.printTree(root.left)
		self.printTree(root.right)






node = TreeNode(4)
node.left = TreeNode(2)
node.right = TreeNode(7)
node.left.left = TreeNode(1)
node.left.right = TreeNode(3)
node.right.left = TreeNode(6)
node.right.right = TreeNode(9)

sol = Solution()
sol.invertTree(node)
sol.printTree(node)

