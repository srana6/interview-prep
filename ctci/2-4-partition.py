"""
Write code to partition a linked list around a value x, such that all nodes less
than x come before all nodes greater than or equal to x.

3  5  8  5  10  2    |    5

3  1  2  10  5  5  8

"""

class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

class Solution(object):

	def partition(self, node, x):
		beforeStart = None
		beforeEnd = None
		afterStart = None
		afterEnd = None

		# Partition
		while node:
			traverse(node)
			
			nodeNext = node.next
			node.next = None

			# Node into end of before
			if node.value < x:
				if not beforeStart:
					beforeStart = node
					beforeEnd = beforeStart
				else:
					beforeEnd.next = node
					beforeEnd = node

			# Node into end of after
			else:
				if not afterStart:
					afterStart = node
					afterEnd = afterStart
				else:
					afterEnd.next = node
					afterEnd = node

			node = nodeNext


		if not beforeStart:
			return afterStart

		beforeEnd.next = afterStart
		return beforeStart


def traverse(head):
	values = []
	aux = head
	while aux:
		values.append(aux.value)
		aux = aux.next

	print (values)


n1 = Node(3)
n2 = Node(5)
n3 = Node(8)
n4 = Node(5)
n5 = Node(10)
n6 = Node(2)
n7 = Node(1)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

part = 5

resp = Solution().partition(n1, part)
traverse(resp)