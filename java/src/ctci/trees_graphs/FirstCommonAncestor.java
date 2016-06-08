package ctci.trees_graphs;

import ctci.linkedlist.ReturnKthLast;

public class FirstCommonAncestor {
	
	public static Node commonAncestor(Node a, Node b){
		if (a == null || b == null) return null;
		
		int delta = depth(b) - depth(a);
		Node first = delta > 0 ? a : b;
		Node second = delta > 0 ? b : a;
		
		second = moveUp(second, Math.abs(delta));
		
		while(first != second && first != null && second != null){
			first = first.parent;
			second = second.parent;
		}
				
		return first == null || second == null ? null : first;
	}
	
	
	
	
	public static int depth(Node node){
		int depth = 0;
		while (node != null){
			depth ++;
			node = node.parent;
		}			
		return depth;
	}
	
	public static Node moveUp(Node node, int levels){
		while (levels > 0 && node != null){
			node = node.parent;
			levels --;
		}
		return node;
	}
	// Everything before works
	
	
	
	
	
	
	public static Node lowestCommonAncestor(Node root, Node p, Node q){
		return null;
	}
	
	
	
	
	
	
	
	// This code seems not to work when nodes are not in tree :
	public static Node findCommonAncestor(Node root, Node node_a, Node node_b){
		Result r = findCommonAncestorHelper(root, node_a, node_b);
		if (r.isAncestor)
			return r.node;
		
		return null;
	}
	
	public static Result findCommonAncestorHelper(Node root, Node node_a, Node node_b) {
		 if (root == null) return new Result(null, false);
		 
		 if (root == node_a && root == node_b) 
			 return new Result(root, true);
		  
		 
		 Result found_left = findCommonAncestorHelper(root.left, node_a, node_b);
		 if (found_left.isAncestor){
			 return found_left;
		 }
		 
		 Result found_right = findCommonAncestorHelper(root.right, node_a, node_b);
		 if (found_right.isAncestor){
			 return found_right;
		 }
		 		 
		 
		 
		 if (found_left != null && found_right != null)
			 return new Result(root, true);
		 
		 else if (root == node_a || root == node_b){
			 boolean isAncestor = found_left.node != null || found_right.node != null;
			 return new Result(root, isAncestor);
		 }
		 else {			 
			 return new Result(found_left != null ? found_left.node : found_right.node, false);
		 }
		 
	 }
	 
	 public static void main(String args[]){		 
		 Node root = new Node(100);
		 root.right = new Node(1000);
		 root.left = new Node(50);
		 root.left.right = new Node(60);
		 root.left.right.left = new Node(59);
		 root.left.right.left.left = new Node(58);
		 root.left.right.left.left.left = new Node(54);
		 
		 root.left.right.left.right = new Node(99);
		 root.left.right.left.right.left = new Node(10);
		 root.left.right.left.right.right = new Node(20);
		 
		 Node a = root.left.right.left.right;
		 Node b = root.left.right.left.right.right;
		 
		 Node c = commonAncestor(a, b);
		 System.out.println(c + "  " + c.value + "  ");
	}
	 
}

class Result {
	Node node;
	boolean isAncestor;
	
	Result(Node node, boolean isAnc){
		this.node = node;
		this.isAncestor = isAnc;
	}
}

class Node {
	 Node parent;
	 Node left;
	 Node right;
	 int value;
	 
	 Node(int value){
		 this.value = value;
	 }
}