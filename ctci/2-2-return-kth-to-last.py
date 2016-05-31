"""
Implement an algorithm to find the kth to last element of a singly linked list.

"""


class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None


def kth_to_last(head, k):
	kth = head
	tail = head

	for i in range(k):
		if not tail: return None
		tail = tail.next

	while tail:
		tail = tail.next
		kth = kth.next

	return kth