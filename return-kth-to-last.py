"""
Implement an algorithm to find the kth to last element of a singly linked list.
"""

class LinkedNode(object):
	def __init__(self, val):
		self.val = val
		self.next = None


def kth_last(root, k):
	p1, p2 = root, root
	size = 0

	while p2:
		size += 1
		p2 = p2.next

	for i in range(size - k):
		p1 = p1.next

	return p1.val

def kth_last2(root, k):
	p1, p2 = root, root

	for i in range(k):
		if not p2: return None
		p2 = p2.next

	while p2:
		p1 = p1.next
		p2 = p2.next

	return p1.val


root = LinkedNode(1)
root.next = LinkedNode(2)
root.next.next = LinkedNode(3)
root.next.next.next = LinkedNode(4)

sol1 = kth_last( root, 1)
sol2 = kth_last2(root, 1)

print (sol1, sol2)



