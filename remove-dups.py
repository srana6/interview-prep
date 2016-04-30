"""
90 - 2.1
Write code to remove duplicates from an unsorted linked list

FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""
from operator import xor
import unittest

class Node(object):
	val = None
	next = None

	def __init__(self, val):
		self.val = val

	def show(self):
		print (self.val)

	def appendToTail(self, val):
		new = Node(val)
		aux = self

		while aux.next is not None:
			aux = aux.next
		aux.next = new
		return True

	@staticmethod
	def deleteNode(node, val):
		aux = node
		if aux.val == val:
			return aux.next

		while aux.next is not None:
			if aux.next.val == val:
				aux.next = aux.next.next
				return node
			aux = aux.next
		return node

	@staticmethod
	def show_all(head):
		res = []
		while head is not None:
			res.append(head.val)
			head = head.next
		return res

def remove_dups(head):
	p1 = head
	p2 = None

	while p1 is not None and p1.next is not None:
		p2 = p1
		while p2 is not None and p2.next is not None:
			if p1.val == p2.next.val:
				p2.next = p2.next.next
			p2 = p2.next
		p1 = p1.next
	return head



class Test(unittest.TestCase):
	root = 10
	childs = {
		'test': [5, 6, 5, 1, 7, 3, 3],
		'expected': [10, 5, 6, 1, 7, 3]
	}

	def test_remove_dups(self):
		head = Node(self.root)
		self.assertEqual(head.val, self.root)

		for child in self.childs['test']:
			head.appendToTail(child)

		remove_dups(head)
		expected = Node.show_all(head)
		self.assertEqual(expected, self.childs['expected'])



if __name__ == '__main__':
	unittest.main()