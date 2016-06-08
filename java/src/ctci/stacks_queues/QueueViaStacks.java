package ctci.stacks_queues;

import java.util.*;

public class QueueViaStacks {
	class MyQueue<T> {
		Stack<T> stackNewest, stackOldest;
		
		public MyQueue(){
			stackNewest = new Stack<T>();
			stackOldest = new Stack<T>();			
		}
		
		public void add(T item){
			stackNewest.push(item);			
		}
		
		public T remove(){
			shiftStacks();		
			return stackOldest.pop();
		}
		
		public int size(){
			return stackNewest.size() + stackOldest.size();
		}
		
		public T peek(){
			shiftStacks();
			return stackOldest.peek();
		}
		
		public void shiftStacks(){
			if (stackOldest.isEmpty()){
				while(!stackNewest.isEmpty()){
					stackOldest.push(stackNewest.pop());
				}
			}
		}
	}
	
}
