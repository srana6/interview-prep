

def wordpattern(pattern, string, memo = {}):    
    if not pattern and not string: return 1
    if (not pattern and string) or (pattern and not string): return 0
    
    size = len(string)
    digit = pattern[0]
    
    if digit in memo:
        current = memo[digit]
        if len(string) < len(current): return 0        
        substring = string[:len(current)]
        
        if substring == current:
            wordpattern(pattern[1:], string[len(current):], memo)
        else:
            return 0
    
    for j in range(1, size + 1):        
        memo[digit] = string[:j]
        if wordpattern(pattern[1:], string[j:], memo): return 1
        memo.pop(digit, None)                
    return 0


pattern = "abbaaabbaa"
string = "redblueblueredredredblueblueredred"

sol = wordpattern(pattern, string)
print ("OUTPUT", sol)