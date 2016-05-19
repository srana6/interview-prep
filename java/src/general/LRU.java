package general;

import java.util.HashMap;

public class LRU {
	class Node {
		int key;
		int value;
		Node prev;
		Node next;
		
		public Node(int key, int value){
			this.key = key;
			this.value = value;
		}
	}
	
	class LRUCache {
		int capacity;
		HashMap<Integer, Node> map = new HashMap<Integer, Node>();
		Node head = null;
		Node end = null;
		
		public LRUCache(int capacity){
			this.capacity = capacity;
		}
		
		public int get(int key){
			if(map.containsKey(key)){
				Node node = map.get(key);
				remove(node);
				
				// Update due to its the latest used
				setHead(node);
				return node.value;
			}
			return -1;
		}
		
		public void remove(Node node){
			if (node.prev != null){
				node.prev.next = node.next;
			}
			else {
				// Most recent is being removed
				head = node.next;
			}
			
			
			if (node.next != null){
				node.next.prev = node.prev;
			}
			else {
				// Least recent being removed
				end = node.prev;
			}
		}
		
		public void setHead(Node node){
			node.next = head;
			node.prev = null;
			
			if (head != null){
				head.prev = node;
			}
			
			head = node;
			
			if (end == null){
				end = head;
			}
		}
		
		public void set(int key, int value){
			if(map.containsKey(key)){
				Node current = map.get(key);
				current.value = value;
				// Latest used, update
				remove(current);
				setHead(current);
			}
			else {
				Node created = new Node(key, value);
				if (map.size() >= capacity){
					map.remove(end.key);
					remove(end);
					setHead(created);
				}
				else {
					setHead(created);
				}
				map.put(key, created);
			}
		}
		
	}	
	
	public static void main(String[] args){
		LRU outer = new LRU();
		LRUCache cache = outer.new LRUCache(20);
	}
	
}
