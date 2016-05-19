package ctci.linkedlist;
/*
 * Implement an algorithm to delete a node in the middle * 
 * 
 */

import ctci.linkedlist.ReturnKthLast.LinkedListNode;

public class DeleteMiddleNode {
	boolean deleteNode(LinkedListNode node){
		if (node == null || node.next == null)
			return false;
		
		LinkedListNode next = node.next;
		node.value = next.value;
		node.next = next.next;		
		return true;		
	}
	
	
	class LinkedListNode {
		int value;
		LinkedListNode next;
		
		LinkedListNode(int value){
			this.value = value;
			this.next = null;
		}
	}
}
