"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Improve using a heap

"""

from heapq import *

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        MAX = float("inf")
        k = len(lists)
        
        smaller = MAX
        index = -1
        
        root = ListNode("")
        aux = root
        
        pointers = [None] * k
        for i in range(k):
            pointers[i] = lists[i]
        
        while True:
            smaller = MAX
            index = -1
            
            for i in range(k):
                curr = MAX if pointers[i] is None else pointers[i].val
                if curr < smaller:
                    smaller = curr
                    index = i
            
            if index == -1:
                break
            else:
                aux.next = ListNode(pointers[index].val)
                aux = aux.next
                pointers[index] = pointers[index].next
                
        return root.next
        