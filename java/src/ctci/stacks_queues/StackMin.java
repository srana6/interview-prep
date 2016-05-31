package ctci.stacks_queues;

public class StackMin {
	class StackWithMin extends Stack<NodeMin> {
		public void push(int value){
			int newMin = Math.min(value, min());
			super.push(new NodeMin(value, newMin));
		}
		
		private int min(){
			if(this.isEmpty()){
				return Integer.MAX_VALUE;
			}
			else{
				return peek().min;
			}
		}
	}	
	
	class NodeMin {
		public int value;
		public int min;
		
		public NodeMin(int value, int min){
			this.value = value;
			this.min = min;
		}
	}
}
