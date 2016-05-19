package leetcode;

import java.util.HashSet;

public class LongestConsecutiveSequence {
	public int longestConsecutive(int[] nums){
		if(nums == null || nums.length == 0) return 0;
		
		int n = nums.length;
		HashSet<Integer> set = new HashSet<>(n);
		for (int num: nums) 
			set.add(num);
		
		int max_len = 0;
		
		for (int num: nums){
			if (set.remove(num)){
				int count = 1;
				int left = num - 1;
				int right = num + 1;
				
				while(set.remove(left)){
					count ++;
					left = left - 1;
				}
				
				while(set.remove(right)){
					count ++;
					right = right + 1;
				}
				
				max_len = Math.max(max_len, count);
			}
		}
		return max_len;
	}
}
