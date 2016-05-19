"""
Design an algorithm to print all permutations of a string. 
For simplicity, assume all characters are unique.
"""

def _permutations(string, perm, n):
    if len(string) == n + 1:
        print (perm)
        return True

    new_char = string[n + 1]
    arr = []
    for i, ielem in enumerate(perm):
        for j, jelem in enumerate(ielem):
            arr.append( ielem[:j] + new_char +  ielem[j:] )
        arr.append(ielem + new_char)
    _permutations(string, arr, n + 1)

def permutations(string):
    if len(string) == 0:
        return False
    _permutations(string, [string[0]], 0)



test = "abcd"
permutations(test)
