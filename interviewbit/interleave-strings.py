"""

"""


class Solution:

    def __init__(self):
        self.A, self.B, self.C = None, None, None
        self.sA, self.sB, self.sC = 0, 0, 0
        self.memo = None

    # greedy approach doesn't work
    def isInterleave_greedy(self, A = [], B = [], C = []):
        sizeA = len(A)
        sizeB = len(B)
        sizeC = len(C)

        if sizeA + sizeB != sizeC: return False

        i, j, k = 0, 0, 0

        while k < sizeA + sizeB:
            a = A[i] if i < sizeA else ' '
            b = B[j] if j < sizeB else ' '

            if C[k] == a:
                i += 1

            elif C[k] == b:
                j += 1

            else:
                print (A[:i + 1], B[:j + 1], C[:k + 1])
                print (A[i], B[j], C[k])
                return False

            k += 1

        return True


    def _isInterleave(self, a, b):
        if a + b == self.sC: return True

        if self.memo[a][b]:
            return self.memo[a][b]

        _a = self.A[a] if a < self.sA else ' '
        _b = self.B[b] if b < self.sB else ' '
        _c = self.C[a + b]

        status = False

        if _a == _c:
            status = self._isInterleave(a + 1, b)

        if _b == _c:
            status |= self._isInterleave(a, b + 1)


        self.memo[a][b] = status

        return status





    def isInterleave(self, A, B, C):
        if A is None or B is None or C is None: return False
        self.A, self.B, self.C = A, B ,C
        self.sA, self.sB, self.sC = map(len, [A, B, C])

        if self.sA + self.sB != self.sC: return False
        self.memo = [[False for _ in range(self.sB + 1)] for __ in range(self.sA + 1)]

        return self._isInterleave(0, 0)






A = "eZCHXr0CgsB4O3TCDlitYI7kH38rEElI"
B = "UhSQsB6CWAHE6zzphz5BIAHqSWIY24D"
C = "eUZCHhXr0SQsCgsB4O3B6TCWCDlAitYIHE7k6H3z8zrphz5EEBlIIAHqSWIY24D"

res = Solution().isInterleave(A, B, C)
print (res)


    

