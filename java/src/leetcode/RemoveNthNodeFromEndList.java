package leetcode;

public class RemoveNthNodeFromEndList {
	
	//Definition for singly-linked list.
	class ListNode {
	    int val;
	    ListNode next;
	    ListNode(int x) { val = x; }
	}
	
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        
        ListNode slow = dummy;
        ListNode fast = dummy;
        
        for(int i = 0; i < n; i++){
            fast = fast.next;
        }
        
        while (fast != null && fast.next !=null){
            slow = slow.next;
            fast = fast.next;
        }
        
        if (slow != null) {
            slow.next = slow.next.next;
        }
        
        return dummy.next;
    }
}