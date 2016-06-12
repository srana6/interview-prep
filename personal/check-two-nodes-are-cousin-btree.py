"""
Check if two nodes are cousins in a Binary Tree
Given the binary Tree and the two nodes say ‘a’ and ‘b’, determine whether the two nodes are cousins of each other or not.

Two nodes are cousins of each other if they are at same level and have different parents.

Example

     6
   /   \
  3     5
 / \   / \
7   8 1   3
Say two node be 7 and 1, result is TRUE.
Say two nodes are 3 and 5, result is FALSE.
Say two nodes are 7 and 5, result is FALSE.




Solution:
	Perform Order level traversal, storing the parent node and level of the parent
	for two nodes to be sibling, their level shall be the same, for instance, the level of their parents
	are equal too.
	As far as two nodes share same level of parents but their parents are different, they are sibling.

	Using a queue, we perform a BFS
	O(n)

"""

from collections import deque

class Node(object):
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value


class BinaryTree(object):
	def __init__(self, root):
		self.root = root

	def isSibling(self, a, b):
		if not a or not b: return False

		# hashmap to track parents of nodes with its level
		parent = {}
		queue = deque([(self.root, 0)])
		found = 0

		# run BFS over whole tree, stop if both nodes were found during traversal
		while queue and found != 2:
			node, level = queue.popleft()

			if node:
				if node in (a, b):
					found += 1

				if node.left: 
					# store parent of child node and its level
					parent[node.left] = (node, level)
					queue.append((node.left, level + 1))

				if node.right:
					# store parent of child node and its level
					parent[node.right] = (node, level)
					queue.append((node.right, level + 1))


		# if both nodes were found, check wether they are siblings or not
		if found == 2:
			node_parent_a, level_parent_a = parent[a]
			node_parent_b, level_parent_b = parent[b]
			if node_parent_a != node_parent_b and level_parent_a == level_parent_b:
				return True

		return False






root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(15)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
 
node1 = root.left.right
node2 = root.right.left

sol = BinaryTree(root).isSibling(node1, node2)
print (sol)

			



print (2 % 0)