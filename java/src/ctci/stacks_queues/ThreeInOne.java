package ctci.stacks_queues;

public class ThreeInOne {
	class FixedMultiStack {
		private int numberOfStacks = 3;
		private int stackCapacity;
		private int[] values;
		private int[] sizes;
		
		public FixedMultiStack (int stackSize){
			stackCapacity = stackSize;
			values = new int[numberOfStacks * stackSize];
			sizes = new int[numberOfStacks];			
		}
		
		public void push(int stackNumber, int value){
			if (isFull(stackNumber)){
				//throw new FullStackException();
			}
			sizes[stackNumber] += 1;			
			int position = indexOfTop(stackNumber);
			values[position] = value;			
		}
		
		public int pop(int stackNumber){
			if(isEmpty(stackNumber)){
				//throw new EmtyStackException();
			}
			int index = indexOfTop(stackNumber);
			int value = values[index];
			values[index] = 0;
			sizes[stackNumber] -= 1;						
			return value;
		}
		
		public boolean isFull(int stackNumber){
			return sizes[stackNumber] == stackCapacity;
		}
		
		public boolean isEmpty(int stackNumber){
			return sizes[stackNumber] == 0;
		}
		
		private int indexOfTop(int stackNumber){
			int offset = stackNumber * stackCapacity;
			int size = sizes[stackNumber];
			return offset + size - 1;
		}
		
		public int peek(int stackNumber){
			if(isEmpty(stackNumber)){
				//throw new EmtyStackException();
			}
			return values[indexOfTop(stackNumber)];
		}
	}
}
