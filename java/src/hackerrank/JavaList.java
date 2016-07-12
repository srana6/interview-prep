package hackerrank;

import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class JavaList {
	
	public static void insert(List<Integer> list, int x, int y){
		list.add(x , y);
	}
	
	public static void delete(List<Integer> list, int x){
		list.remove(x);
	}
	
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        List<Integer> list = new LinkedList<Integer>();
        
        for (int i = 0; i < n ; i++){
        	list.add(sc.nextInt());
        }
        
        int operations = sc.nextInt();
        
        for (int i = 0; i < operations ; i++){
        	String operation = sc.next();
        	
        	if (operation.equals("Insert")){
        		int x = sc.nextInt();
        		int y = sc.nextInt();
        		
        		insert(list, x, y);
        	}
        	else {
        		int x = sc.nextInt();
        		
        		delete(list, x);
        	}
        }
        
        for (int i = 0; i < list.size() ; i++){
            System.out.print(list.get(i) + " ");
        }
    }
}
