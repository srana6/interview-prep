package general;

import java.util.*;

public class FindDuplicates {
	
	public static ArrayList<Integer> findAllDuplicates(int[] arr){
		HashSet<Integer> result = new HashSet<Integer>();
		
		for(int i = 0; i < arr.length; i++){
			int elem = Math.abs(arr[i]);
			
			if (arr[elem] > 0){
				arr[elem] *= -1;
			}
			else {
				result.add(elem);
			}
		}
		
		return new ArrayList<Integer>(result);
	}

	public static void main(String[] args){
		int[] arr = {1, 2, 3, 1, 3, 6, 6, 1, 7, 3};
		
		List<Integer> res = findAllDuplicates(arr);
		System.out.println(res);
	}
}