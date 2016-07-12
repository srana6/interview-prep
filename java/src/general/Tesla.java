package general;

import java.util.HashMap;
import java.util.HashSet;

public class Tesla {
	static class Solution {
		
		static int longestChain(String[] arr) {
            int n = arr.length;
            HashSet<String> set = new HashSet<String>();
            HashMap<String, Integer> cache = new HashMap<String, Integer>();
            
            for(int i=0; i< n; i++){
                    set.add(arr[i]);
            }
        
            int longest = 0;
            for(int i=0; i<n; i++){                
                   longest = Math.max(longestStep(arr[i], arr, set, 1, cache),longest);
            }
            return longest;
	    }
		
		
		
	    static int longestStep(String curWord, String[] arr, HashSet<String> set, int step, HashMap<String, Integer> cache){
	    		if (cache.containsKey(curWord))
	    			return cache.get(curWord);
	    		
	    		System.out.println(curWord + "    "  +  step);
	    		
	            int max_step = step;
	            for(int i=0; i < curWord.length(); i++){
	                    String newStr = curWord.substring(0,i) + curWord.substring(i+1);
	                    if(set.contains(newStr)){
	                    	max_step = Math.max(longestStep(newStr,arr, set, step + 1, cache), max_step);
	                    }
	            }
	            
	            cache.put(curWord, max_step);
	            return max_step;
	    }
	}
	
	
	public static void main(String[] args) {
		String[] test = {
				"a",
			    "b",
			    "ba",
			    "bca",
			    "bda",
			    "bdca"};
		
		int solution = Solution.longestChain(test);
		
		System.out.println(solution);

	}

}
