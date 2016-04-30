import unittest

"""
Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""


class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def isSameTree(self, p, q):
		pNone = (p is not None)
		qNone = (q is not None)		

		if pNone == qNone:
			if pNone and qNone:
				if p.val != q.val:					
					return False					
				left = self.isSameTree(p.left, q.left)
				if not left:
					return False
				right = self.isSameTree(p.right, q.right)
				if not right:
					return False
			return True		
		return False

	def isSameTree2(self, p, q):
		if p and q:
			return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
		return p == q
	
class Test(unittest.TestCase):

	def test_isSameTree_False(self):
		sol = Solution()

		rootA = TreeNode(1)
		rootA.left = TreeNode(2)
		rootA.right = TreeNode(3)
		rootA.left.left = TreeNode(4)
		rootA.left.right = TreeNode(5)

		rootB = TreeNode(1)
		rootB.right = TreeNode(3)

		res = sol.isSameTree(rootA, rootB)
		self.assertFalse(res)

	def test_isSameTree_True(self):
		sol = Solution()

		rootA = TreeNode(1)
		rootA.left = TreeNode(2)
		rootA.right = TreeNode(3)
		rootA.left.left = TreeNode(4)
		rootA.left.right = TreeNode(5)

		rootB = TreeNode(1)
		rootB.left = TreeNode(2)
		rootB.right = TreeNode(3)
		rootB.left.left = TreeNode(4)
		rootB.left.right = TreeNode(5)

		res = sol.isSameTree(rootA, rootB)
		self.assertTrue(res)

	def test_isSameTree_True(self):
		sol = Solution()

		rootA = TreeNode(10)
		rootA.left = TreeNode(5)
		rootA.right = TreeNode(15)

		rootB = TreeNode(10)
		rootB.left = TreeNode(5)		
		rootB.left.right = TreeNode(15)

		res = sol.isSameTree(rootA, rootB)
		self.assertFalse(res)

if __name__ == '__main__':
	unittest.main()
