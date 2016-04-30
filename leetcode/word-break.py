"""
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""

# Brute force First solution.
# Breaks with following input

class Solution(object):
    def wordBreak(self, s, wordDict):
        if not s:            
            return True
        
        for i in range(len(s) + 1):
            if s[:i] in wordDict:
                if self.wordBreak(s[i:], wordDict):
                    return True
        return False   


s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
d = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

print (s, d)
print ()


sol = Solution()
res = sol.wordBreak(s, d)
print (res)


