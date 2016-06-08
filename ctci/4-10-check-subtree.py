"""
T1 and T2 are two very large binary trees, with T1 much bigger than T2. 
Create an algorithm to determine if T2 is subtree of T1.

A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.

Analysis:
	How to compare tree_a  vs  tree_b

	Two trees are the same if they have same pre-order traversal.  (including null as values)
"""

class Node(object):
	def __init__(self, val):
		self.left = None
		self.right = None
		self.data = val


class Solution1(object):
	def check_subtree(self, root_a, root_b):
		a_preorder = "".join(self.get_pre_order(root_a, []))
		b_preorder = "".join(self.get_pre_order(root_b, []))

		return a_preorder.find(b_preorder) != -1

	def get_pre_order(self, root, result):
		if not root: 
			result.append('x')
			return result

		result.append(str(root.data))
		self.get_pre_order(root.left, result)
		self.get_pre_order(root.right, result)

		return result




# Better runtime complexity. O(n + km)  , where k is the matching roots in the tree
class Solution2(object):

	def contains_tree(self, root_a, root_b):
		if not root_a: return False
		return self.subtree(root_a, root_b)


	def subtree(self, root_a, root_b):
		if not root_a: return False
		if root_a.data == root_b.data and self.match_tree(root_a, root_b):
			return True
		return self.subtree(root_a.left, root_b) or self.subtree(root_a.right, root_b)


	def match_tree(self, root_a, root_b):	
		if not root_a and not root_b: return True
		elif not root_a or not root_b: return False
		elif root_a.data != root_b.data: return False	
		return self.match_tree(root_a.left, root_b.left) and self.match_tree(root_a.right, root_b.right)





root = Node(50)
root.left = Node(20)
root.right = Node(60)

root.left.left = Node(10)
root.left.right = Node(25)

root2 = Node(999)
root2.left = Node(998)
root2.right = root


result = Solution1().get_pre_order(root, [])
print (result)

print ( Solution1().check_subtree(root2, root) )
print ( Solution2().contains_tree(root2, root) )