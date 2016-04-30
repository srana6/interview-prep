class Solution(object):
    def checkPalindrome(self, string, start, end):
        midIndex = (start + end) // 2
        
        while start <= end and string[start] == string[end - 1]:
            start += 1
            end -= 1
    
        if start >= end:
            return True
        
        return False
    
    def longestPalindrome(self, string):
        """
        :type s: str
        :rtype: str
        """
        longest = 0
        palindrome = ""
        
        n = len(string)
        for i in range(n):
            j = i
            k = n
            while j < k:
                #print ("call", palindrome)

                if self.checkPalindrome(string, j, k) and k - j > longest:
                    palindrome = string[j:k]
                    longest = k - j
                k -= 1
                
        return palindrome

string = "jhgtrclvzumufurdemsogfkpzcwgyepdwucnxrsubrxadnenhvjyglxnhowncsubvdtftccomjufwhjupcuuvelblcdnuchuppqpcujernplvmombpdttfjowcujvxknzbwmdedjydxvwykbbamfnsyzcozlixdgoliddoejurusnrcdbqkfdxsoxxzlhgyiprujvvwgqlzredkwahexewlnvqcwfyahjpeiucnhsdhnxtgizgpqphunlgikogmsffexaeftzhblpdxrxgsmeascmqngmwbotycbjmwrngemxpfakrwcdndanouyhnnrygvntrhcuxgvpgjafijlrewfhqrguwhdepwlxvrakyqgstoyruyzohlvvdhvqmzdsnbtlwctetwyrhhktkhhobsojiyuydknvtxmjewvssegrtmshxuvzcbrabntjqulxkjazrsgbpqnrsxqflvbvzywzetrmoydodrrhnhdzlajzvnkrcylkfmsdode"

print ( Solution().longestPalindrome(string) )