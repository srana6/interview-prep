"""
.237
Write a function to delete a node (except the tail) in a singly 
linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the 
third node with value 3, the linked list should become 1 -> 2 -> 4 after 
calling your function.
"""

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def deleteNode(self, node):
		nextNode = node.next
		node.val = nextNode.val
		node.next = nextNode.next



# Test case
rootTest = ListNode(1)
rootTest.next = ListNode(2)
child1Test = rootTest.next
child1Test.next = ListNode(3)
child2Test = child1Test.next
child2Test.next = ListNode(4)

sol = Solution()
sol.deleteNode(child2Test)

node = rootTest
while node:
	print (node.val)
	node = node.next



