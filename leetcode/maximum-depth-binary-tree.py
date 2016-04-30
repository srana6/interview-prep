""" 
.104
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along 
the longest path from the root node down to the farthest leaf node.
"""

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def maxDepth(self, node):
		if node is None: 
			return 0
		left = self.maxDepth(node.left)
		right = self.maxDepth(node.right)
		return max(left, right) + 1


node0 = TreeNode(10)
node0.left = TreeNode(5)
node0.right = TreeNode(15)
node1 =  node0.right
node1.left = TreeNode(12)
node2 = node1.left
node2.right = TreeNode(13)

sol = Solution()
res = sol.maxDepth(node0)
print (res)