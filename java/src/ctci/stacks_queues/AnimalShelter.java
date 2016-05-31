package ctci.stacks_queues;

import java.util.LinkedList;

public class AnimalShelter {
	abstract class Animal {
		private int order;
		private String name;
		
		
		public Animal (String name){
			this.name = name;
		}
		
		public void setOrder(int order){
			this.order = order;
		}
		
		public int getOrder(){
			return this.order;
		}
		
		public boolean isOlderThan(Animal other){
			return this.getOrder() < other.getOrder();
		}
	}
	class Dog extends Animal {
		public Dog(String name){
			super(name);
		}
	}
	
	class Cat extends Animal {
		public Cat(String name){
			super(name);
		}
	}
	
	class AnimalQueue {
		LinkedList<Dog> dogs = new LinkedList<>();
		LinkedList<Cat> cats = new LinkedList<>();
		private int order = 0;
		
		public void enqueue(Animal animal){
			animal.setOrder(order);
			order ++;
			
			if (animal instanceof Dog){
				dogs.addLast((Dog)animal);
			}
			else if(animal instanceof Cat){
				cats.addLast((Cat)animal);
			}
		}
		
		public Animal enqueueAny(){
			if (dogs.size() == 0){
				return dequeueCats();
			}
			else if(cats.size() == 0){
				return dequeueDogs();
			}
			
			Dog dog = dogs.peek();
			Cat cat = cats.peek();
			
			if (dog.isOlderThan(cat)){
				return dequeueDogs();
			}
			else{
				return dequeueCats();
			}
			
		}
		
		public Cat dequeueCats(){
			return cats.poll();
		}
		
		public Dog dequeueDogs(){
			return dogs.poll();
		}
	}
}
