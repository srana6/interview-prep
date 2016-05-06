"""
Sort a linked list in O(n log n) time using constant space complexity.

Incomplete

"""
class Solution(object):
    
    def mergeSort(self, head, end):
        mid, tail = head, head
        
        while tail and tail.next and tail.next != end:
            mid = mid.next
            tail = tail.next.next
        
        mergeSort(head, mid)
        mergeSort(mid, end)
        
        
        
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: 
            return head

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next



vowels = set(["a", "e", "i", "o", "u"])

if "a" in vowels:
    print ("YE")