package ctci.trees_graphs;

import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.Queue;

public class RouteBetweenNodes {
	enum State {Unvisited, Visited, Visiting};
	
	public boolean search(Graph graph, Node start, Node end){
		if (start == end){
			return true;
		}
		
		LinkedList<Node> queue = new LinkedList<>();
		
		ListIterator<Node> iterator = queue.listIterator();
				
		for (Node node: graph.nodes){
			node.state = State.Unvisited;
		}
		start.state = State.Visited;
		queue.add(start);
		
		while (!queue.isEmpty()){
			Node source = queue.removeFirst();
			if (source != null){
				for (Node adj : source.children){
					if(adj.state == State.Unvisited){
						if (adj == end){
							return true;
						}
						else {
							adj.state = State.Visiting;
							queue.add(adj);
						}						
					}
				}
			}
		}
		
		return false;
	}	
	
	
	class Graph {
		public Node[] nodes;
	}
	
	class Node {
		public String name;
		public State state;
		public Node[] children;
	}
	
}
