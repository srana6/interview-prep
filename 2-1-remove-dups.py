"""
Remove Dups

Write code to remove duplicates from an unsorted linked list

No temporary buffer allowed
"""



class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None


def remove_duplicates(head):
	if not head: return 
	aux = head
	dup = None

	while aux:
		dup = aux

		while dup and dup.next:
			if dup.next.value == aux.value:
				dup.next = dup.next.next
			dup = dup.next

		aux = aux.next


