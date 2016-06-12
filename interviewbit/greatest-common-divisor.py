"""

"""


class Solution:
    # fast.  logarithmic time
    def gcd2(self, A, B):
        print (A, B)

        if B == 0:
            return A

        return self.gcd2(B, A % B)

    # slower.   O(min(A, B))
    def gcd(self, A, B):
        if 0 in (A, B): return max(A, B)
        
        m = A if A > B else B
        n = B if A > B else A

        if m > n: m = m - n
                
        for divisor in reversed(range(2, min(m, n) + 1)):
            print (divisor)

            if m % divisor == 0 and n % divisor == 0:
                return divisor
                
        return 1


a = 9000
b = 4000

sol = Solution().gcd2(a, b)
print (sol)