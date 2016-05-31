"""
You are given two linked lists representing two non-negative numbers. The digits are stored in 
reverse order and each of their nodes contain a single digit. Add the two numbers and return it 
as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if not l1 and not l2: return None
        if l1 and not l2: return l1
        if l2 and not l1: return l2
        
        dummy = ListNode(' ')
        aux = dummy
        a = l1
        b = l2
        remainder = 0
        
        # iterate over there are not more numbers in the lists, or there is something carried
        while a or b or remainder > 0:
            val_a = 0
            val_b = 0
            
            if a:
                val_a = a.val
                a = a.next
            
            if b:
                val_b = b.val
                b = b.next
            
            # get value and result
            total = val_a + val_b + remainder
            result = total % 10

            # update number to carry for next iteration
            remainder = 0 if total < 10 else 1
            
            aux.next = ListNode(result)
            aux = aux.next
        return dummy.next