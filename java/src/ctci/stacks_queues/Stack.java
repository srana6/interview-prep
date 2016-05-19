package ctci.stacks_queues;

import java.util.EmptyStackException;

public class Stack<T>{
	private static class StackNode<T>{
		private T data;
		private StackNode<T> next;
		
		private StackNode(T data){
			this.data = data;
		}
	}
	
	private StackNode<T> top;
	
	
	public T pop(){
		if(top == null){
			throw new EmptyStackException();
		}
		T item = top.data;
		top = top.next;
		return item;
	}
	
	
	public void push(T item){
		StackNode<T> node = new StackNode<T>(item);
		node.next = top;
		top = node;		
	}
	
	public T peek(){
		if (top == null){
			throw new EmptyStackException();
		}
		T item = top.data;
		return item;
	}
	
	public boolean isEmpty(){
		return top == null;
	}
}