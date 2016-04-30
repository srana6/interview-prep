"""

Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37

"""

import unittest
import sys

class Solution(object):
    def compareVersion(self, version1, version2):
        v1 = [int(i) for i in version1.split('.')]
        v2 = [int(i) for i in version2.split('.')]

        size1, size2 = len(v1), len(v2)
        num1, num2 = 0, 0        

        for i in range(max(size1, size2)):
            num1 = v1[i] if i < size1 else 0
            num2 = v2[i] if i < size2 else 0

            if num1 > num2: return 1
            elif num1 < num2: return -1
            
        return 0


class Test(unittest.TestCase):
    def test_compareVersion(self):
        v1 = "1.0"
        v2 = "1"

        sol = Solution()
        res = sol.compareVersion(v1, v2)

        print ('sol', res)
        
unittest.main()