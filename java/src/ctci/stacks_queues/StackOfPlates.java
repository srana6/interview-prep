package ctci.stacks_queues;

import java.util.*;

public class StackOfPlates {
	class SetOfStacks {
		ArrayList<Stack> stacks;
		int capacity;
		
		public SetOfStacks(int capacity){
			this.stacks = new ArrayList<>();
			this.capacity = capacity;
		}
		
		public void push(int item){
			Stack last = getLastStack();
			if (last != null && !last.isFull()){
				last.push(item);
			}
			else{
				Stack stack = new Stack(capacity);
				stack.push(item);
				stacks.add(stack);
			}
		}
		
		public int pop(){
			Stack last = getLastStack();
			if (last == null){
				throw new EmptyStackException();
			}
			
			int latest = last.pop();
			return latest;
		}
		
		public boolean isEmpty(){
			Stack last = getLastStack();
			return last == null;
		}
		
		public Stack getLastStack(){
			if (stacks.size() == 0) return null;
			return stacks.get(stacks.size() - 1);			
		}
		
		class Stack {
			private int capacity;
			private Node top, bottom;
			int size = 0;
			
			public Stack(int capacity){
				this.capacity = capacity;
			}
			
			public int pop() {
				// TODO Auto-generated method stub
				return 0;
			}

			public boolean isFull() {
				// TODO Auto-generated method stub
				return false;
			}

			public boolean push(int v){
				if (size >= capacity){
					return false;
				}
				size ++;
				Node node = new Node(v);
				if (size == 1)
					bottom = node;
				//join(node, top);
				top = node;
				return true;
			}
			
			/*
			private void join(Node above, Node below) {
				if (below != null) below.above = above;
				if (above != null) above.below = below;
			}
			*/

			class Node {				
				Node next;
				int elem;
				
				public Node (int elem){
					this.elem = elem;
				}
			}
		}
		
	}
	
	public static void main(String[] args) {
		

	}

}
