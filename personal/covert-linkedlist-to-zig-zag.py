class Node:
	def __init__(self, val):
		self.next = None
		self.value = val



def zigzag(head):
	if not head: return None
	order = True
	dummy = Node('')
	dummy.next = head

	prev, curr, nextn = dummy, head, head.next

	while curr and nextn:
		if not check_order(curr.value, nextn.value, order):
			swap_nodes(prev, curr, nextn)
			curr, nextn = nextn, curr

		order = not order
		prev = prev.next
		curr = curr.next
		nextn = nextn.next

	return dummy.next



def check_order(a, b, order):
	if order:
		return a < b
	else:
		return a > b

def swap_nodes(prev, a, b):
	aux = b.next
	prev.next = b
	b.next = a
	a.next = aux

def print_nodes(head):
	res = []
	while head:
		res.append(head.value)
		head = head.next
	return res

head = Node(4)
head.next = Node(3)
head.next.next = Node(7)
head.next.next.next = Node(8)
head.next.next.next.next = Node(6)
head.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next = Node(1)

zhead = zigzag(head)
res = print_nodes(zhead)
print (res)