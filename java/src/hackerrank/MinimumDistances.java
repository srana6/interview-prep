package hackerrank;
import java.util.*;

public class MinimumDistances {
	public static int findMin(HashMap<Integer, ArrayList<Integer>> map) {
        int min = Integer.MAX_VALUE;
        
        for (Map.Entry<Integer, ArrayList<Integer>> entry : map.entrySet()){
            ArrayList<Integer> list_num = entry.getValue();
            for (int i = 0; i < list_num.size() - 1 ; i ++){
                int distance = Math.abs(list_num.get(i) - list_num.get(i + 1));
                
                min = Math.min(min, distance);
            }            
        }
        
        return min == Integer.MAX_VALUE ? -1 : min;
    }
    
    public static int solution(int[] arr){
        if (arr == null || arr.length == 0) return -1;
        HashMap<Integer, ArrayList<Integer>> map = new HashMap<Integer, ArrayList<Integer>>();
        
        for(int i = 0; i < arr.length; i++){
            int num = arr[i];
            
            if (!map.containsKey(num))
                map.put(num, new ArrayList<Integer>());
            
            ArrayList<Integer> list_num = map.get(num);
            list_num.add(i);            
        }
        return findMin(map);        
    }
    
    public static int solution2(int[] arr){
    	int min = Integer.MAX_VALUE;
    	
    	for(int i = 0; i < arr.length; i++){
    		for (int j = 0; j < arr.length; j++){
    			if (i != j && arr[i] == arr[j]){
    				int distance = Math.abs(i - j);
    				min = Math.min(min, distance);
    			}    				
    		}
    	}
    			
    	return min == Integer.MAX_VALUE ? -1 : min;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int A[] = new int[n];
        for(int A_i=0; A_i < n; A_i++){
            A[A_i] = in.nextInt();
        }
        
        int sol = solution(A);
        System.out.println(sol);
    }
}
