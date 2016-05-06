class Solution(object):
    
    def __init__(self):
        self.memo = {}
        self.memo[1] = "1"
        
    def getNewSeq(self, string):
        sequence = []
        n = len(string)
        
        curr = None
        freq = 0
        i = 0
        
        while i < n + 1:
            if freq > 0:
                sequence.append(str(freq))
                sequence.append(curr)
                
                if i == n:
                    break
            
            curr = string[i]
            freq = 0
            
            while i < n and string[i] == curr:
                freq += 1
                i += 1
        
        return "".join(sequence)
        
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1: return ""
        if n in self.memo: 
            return self.memo[n]
            
        computed = len(self.memo)
        
        for i in range(computed + 1, n + 1):
            prev = self.memo[i - 1]
            self.memo[i] = self.getNewSeq(prev)
            
        return self.memo[n]
        

Solution().countAndSay(4)
