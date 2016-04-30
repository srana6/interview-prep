"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""



class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def deleteDuplicates(self, head):
		p1 = head
		p2 = None		
		while p1 and p1.next:
			p2 = p1.next
			duplicate = False
			root = False

			if head.val == p2.val:
				p2 = p1
				root = True

			while p2.next and p2.val == p2.next.val:
				p2 = p2.next
				duplicate = True

			if duplicate:
				p1.next = p2.next

				if root:
					head = p2.next
			else:
				p1 = p1.next
		return head

	def deleteDuplicates_better(self, head):
		dummy = ListNode(0)
		head, dummy.next = dummy, head
		p1 = None

		while head and head.next:
			p1 = head.next
			duplicate = False

			while p1.next and p1.val == p1.next.val:
				p1 = p1.next
				duplicate = True

			if duplicate:
				head.next = p1.next
			else:
				head = head.next
		return dummy.next

	def printList(self, head):
		p1 = head
		while p1:
			print (p1.val)
			p1 = p1.next


test = ListNode(1)
test.next = ListNode(1)
test.next.next = ListNode(2)
test.next.next.next = ListNode(3)
test.next.next.next.next = ListNode(4)
test.next.next.next.next.next = ListNode(4)
test.next.next.next.next.next.next = ListNode(4)

sol = Solution()
result = sol.deleteDuplicates(test)
sol.printList(result)




