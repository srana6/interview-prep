"""
LinkedList

Merge k Sorted Lists
Difficulty: Hard
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

"""

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


from heapq import *
class Solution(object):
	def mergeKLists(self, lists):
		if not lists: return None
		k = len(lists)
		heap = []
		dummy = ListNode(-1)
		tail = dummy

		for i in range(k):
			if lists[i]:
				heappush(heap, (lists[i].val, lists[i]))
				
		while heap:
			print (heap)
			val, node = heappop(heap)
			tail.next = node
			tail = tail.next
			node = node.next
			if node:
				heappush(heap, (node.val, node))

		return dummy.next