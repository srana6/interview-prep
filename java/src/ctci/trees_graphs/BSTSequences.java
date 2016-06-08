package ctci.trees_graphs;

import java.util.*;

public class BSTSequences {
	
	
	
	static ArrayList<LinkedList<Integer>> allSequences(TreeNode node){
		ArrayList<LinkedList<Integer>> result = new ArrayList<LinkedList<Integer>>();
		
		if (node == null){
			result.add(new LinkedList<Integer>());
			return result;
		}
		
		LinkedList<Integer> prefix = new LinkedList<Integer>();
		prefix.add(node.data);
		
		ArrayList<LinkedList<Integer>> left_seq = allSequences(node.left);
		ArrayList<LinkedList<Integer>> right_seq = allSequences(node.right);
				
		for (LinkedList<Integer> left : left_seq){
			for (LinkedList<Integer> right : right_seq) {
				ArrayList<LinkedList<Integer>> weaved = new ArrayList<LinkedList<Integer>>();
				weaveLists(left, right, weaved, prefix);
				result.addAll(weaved);
				
			}
		}
		
		return result;
	}
	
	
	static void weaveLists(LinkedList<Integer> first, LinkedList<Integer>  second, 
					ArrayList<LinkedList<Integer>> results, LinkedList<Integer> prefix){
		
		if (first.size() == 0 || second.size() == 0){
			LinkedList<Integer> result = (LinkedList<Integer>) prefix.clone();
			result.addAll(first);
			result.addAll(second);
			results.add(result);
			return;
		}
		
		int headFirst = first.removeFirst();
		prefix.addLast(headFirst);
		weaveLists(first, second, results, prefix);
		prefix.removeLast();
		first.addFirst(headFirst);
		
		int headSecond = second.removeFirst();
		prefix.addLast(headSecond);
		weaveLists(first, second, results, prefix);
		prefix.removeLast();
		second.addFirst(headSecond);
	}
	
	public static void main(String args[]){
		TreeNode root = new TreeNode(50);
		root.left = new TreeNode(20);
		root.right = new TreeNode(60);
		
		root.left.left = new TreeNode(10);
		root.left.right = new TreeNode(25);
		
		/*
		
		root.right.right = new TreeNode(70);
		
		root.left.left.left = new TreeNode(5);
		root.left.left.right = new TreeNode(15);
		
		root.right.right.left = new TreeNode(65);
		root.right.right.right = new TreeNode(80);
		
		*/
		
		
		ArrayList<LinkedList<Integer>> result = allSequences(root);
		
		for (LinkedList<Integer> subList : result){
			System.out.println(subList);
		}
		
	}
	
}


class TreeNode {
	TreeNode left;
	TreeNode right;
	int data;
	
	TreeNode(int val){
		data = val;
	}
}