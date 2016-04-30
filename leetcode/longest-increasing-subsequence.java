public class Solution {
    public int lengthOfLIS(int[] nums) {
        if (nums == null || nums.length == 0)
            return 0;
            
        int N = nums.length;
        int[] cache = new int[N];
        int longest_sub = 0;
        // Each number has a subsequence of 1, which means itself
        Arrays.fill(cache, 1);
        
        // Compute and cache longest sub sequence
        for (int i = 1 ; i < N ; i++){
            for (int j = 0 ; j < i ; j++){

                // Make sure each previous number is smaller
                if (nums[j] < nums[i]){

                    // Store the max sub sequence only
                    cache[i] = Math.max(cache[i], cache[j] + 1);
                }
            }
        }
        
        // Get the longest sub sequence already computed
        for (int i = 0 ; i < cache.length ; i++)
            longest_sub = Math.max(longest_sub, cache[i]);
            
        return longest_sub;
    }
}