"""
Implement a function to check if a binary tree is balanced. For the purposes of this question, 
a balanced tree is defined to be a tree such that the height of the two subtrees of any node 
never differ by more than one
"""

class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def checkBalanced(node):
	if node:
		sleft, hleft = checkBalanced(node.left)
		sright, hright = checkBalanced(node.right)
		if abs(hleft - hright) > 1 or not sleft or not sright:
			return (False, 0)	
		return (True, max(hleft, hright) + 1)
	return (True, -1)


root = TreeNode(50)
root.left = TreeNode(17)
root.right = TreeNode(76)
root.right.left = TreeNode(54)
root.left.left = TreeNode(9)
root.left.right = TreeNode(23)
root.left.right.left = TreeNode(19)

print( checkBalanced(root) ) 

	



