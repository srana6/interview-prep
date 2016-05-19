package ctci.linkedlist;

public class ReturnKthLast {
	public LinkedListNode nthToLst(LinkedListNode head, int k){
		LinkedListNode p1 = head;
		LinkedListNode p2 = head;
		
		for (int i = 0; i < k ; i++){
			if (p1 == null){
				return null;
			}			
			p1 = p1.next;
		}
		
		while (p1 != null){
			p1 = p1.next;
			p2 = p2.next;
		}
		
		return p2;
	}
	
	public void solution(){
		System.out.println("YAY");
		
		LinkedListNode n1 = new LinkedListNode(1);
		LinkedListNode n2 = new LinkedListNode(2);
		LinkedListNode n3 = new LinkedListNode(3);
		LinkedListNode n4 = new LinkedListNode(4);
		LinkedListNode n5 = new LinkedListNode(5);
		
		n1.next = n2;
		n2.next = n3;
		n3.next = n4;
		n4.next = n5;
		
		nthToLst(n1, 2);
	}
	
	class LinkedListNode {
		int value;
		LinkedListNode next;
		
		LinkedListNode(int value){
			this.value = value;
			this.next = null;
		}
	}
	
	public static void main(String args[]){
		ReturnKthLast problem = new ReturnKthLast();
		problem.solution();
	}
	
	
}
