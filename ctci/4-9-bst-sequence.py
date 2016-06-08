"""
A binary search tree was created by traversing through an array from left to right and inserting each element.
Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.

Advice: Trust and focus

"""

from copy import deepcopy
from collections import deque

class Node(object):
	def __init__(self, val):
		self.left = None
		self.right = None
		self.data = val


def all_sequences(root):	
	if not root: return [deque()]

	result = []
	prefix = deque([root.data])

	left_seq = all_sequences(root.left)
	right_seq = all_sequences(root.right)

	for lseq in left_seq:
		for rseq in right_seq:
			weaved = []
			weave(lseq, rseq, prefix, weaved)
			result.extend(weaved)
	return result


def weave(first, second, prefix, result):
	if not first or not second:
		temp = deepcopy(prefix)
		temp.extend(first)
		temp.extend(second)
		result.append(temp)
		return


	head_first = first.popleft()
	prefix.append(head_first)
	weave(first, second, prefix, result)
	first.appendleft(prefix.pop())

	head_second = second.popleft()
	prefix.append(head_second)
	weave(first, second, prefix, result)
	second.appendleft(prefix.pop())



root = Node(50)
root.left = Node(20)
root.right = Node(60)

root.left.left = Node(10)
root.left.right = Node(25)

result = all_sequences(root)


for row in result:
	print (row)
