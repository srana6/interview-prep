"""
Compare Version Numbers


Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37

"""

class Solution(object):
    def compareVersion(self, version1, version2):
        v1 = [int(elem) for elem in version1.split('.')]
        v2 = [int(elem) for elem in version2.split('.')]
        
        n = len(v1)
        m = len(v2)
        
        # Using max allows to iterate over the longer
        for i in range(max(n, m)):

            # Fallback on 0 if there is version left.  1.0 == 1.0.0
            elem1 = v1[i] if i < n else 0
            elem2 = v2[i] if i < m else 0
            
            if elem1 > elem2:
                return 1
                
            elif elem1 < elem2:
                return -1
        
        return 0