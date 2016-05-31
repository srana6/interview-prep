"""
Given a string s and a dictionary of words dict, determine if s can be segmented into a 
space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".


"""

from collections import deque

class Solution(object):

    # 2^n
    def wordBreak(self, string, wordDict):        
        if string in wordDict:
            return True
        
        for i in range(1, len(string)):
            subA = string[:i]
            subB = string[i:]
            
            if subA in wordDict and self._wordBreak(subB, wordDict):
                return True
            
        return False

    # n^2 DP
    def wordBreak(self, string, wordDict):
        if not string or not wordDict: return False
        n = len(string)
        memo = [False] * (n + 1)
        memo[0] = True

        for j in range(1, n + 1):
            for i in range(j):
                if memo[i] and string[i:j] in wordDict:
                    memo[j] = True

        print (memo)

    # n^2  using BFS
    def wordBreak(self, string, wordDict):
        if string in wordDict: return True
        n = len(string)
        queue = deque([0])
        visited = set()
        visited.add(0)

        while queue:
            i = queue.popleft()
            
            for j in range(i + 1, n + 1):
                if j in visited: continue

                if string[i:j] in wordDict:
                    if j == n:
                        return True

                    queue.append(j)
                    visited.add(j)

        return False


    # incomplete
    def wordBreak(self, string, wordDict):
        if string in wordDict: return True
        n = len(string)
        memo = [False] * (n + 1)
        memo[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                print (j, i, string[j:i])

        return memo[n]



wordDict = set(["night","mare","lol","hi"])
string = "nighthilol"

ans = Solution().wordBreak(string, wordDict)
print (ans)

