# Complete the function below.
"""
Directions:
    N
W       E
    S

"""

# We use a hashmap to quickly get the next movements incrementals
movements = {}
movements['NG'] = (0,  1)
movements['SG'] = (0, -1)
movements['WG'] = (-1, 0)
movements['EG'] = (0,  1)

# Array of directions
directions = ['N', 'E', 'S', 'W']

# Update and change direction either left or right using module
def change_direction(i, incr):
    index = (i + incr) % 4
    return index

# Update movement
def move(pos, movement):
    pos[0] += movement[0]
    pos[1] += movement[1]

def  doesCircleExist(commands):
    pos = [0, 0]
    direction = 0
    command = 'G'
    
    for i in range(4):
        for curr_command in commands:
            if curr_command == 'G':
                move(pos, movements[directions[direction] + 'G'])

            elif curr_command == 'L':
                direction = change_direction(direction, -1)

            elif curr_command == 'R':
                direction = change_direction(direction, 1)
    
    if pos == [0, 0] and direction == 0:
        return "YES"
    
    return "NO"
            
            
    










from collections import deque


def longest_palindrome(string, res, p, i, j, palindromes):
    size = len(string)
    res = deque(res)
    
    while i >= 0 and j < size:
        if string[i] == string[j]:
            res.appendleft(string[i])
            res.append(string[j])
            palindromes.add("".join(res))
            i -= 1
            j += 1
        else:            
            break
    

def palindrome(string):
    if not string: return 0
    
    # Set used to only store distinct elements
    palindromes = set()
    
    size = len(string)
    
    for i in range(size):
        pivot = string[i]
        
        # Every single letter is a palindrome itself
        palindromes.add(pivot)
        
        # Even palindrome
        l_even = longest_palindrome(string, [], i, i, i + 1, palindromes)
        
        # Odd palindrome
        l_odd = longest_palindrome(string, [pivot], i, i - 1, i + 1, palindromes)
            
    return len(palindromes)
                
        
    
    
    


from collections import deque

def bfs(start, words):
    chain = 0    
    queue = deque([(start, 1)])

    while queue:
        word, length = queue.popleft()

        chain = max(chain, length)

        w_size = len(word)
        for i in range(w_size):
            substring = word[:i] + word[i + 1:]
            if substring in words:
                queue.append((substring, length + 1))

    return chain




    

def longestChain(words):
    if not words: return 0        
    size = len(words)
    words = set(words)
    longest = 0

    for word in words:
        longest = max(longest, bfs(word, words))

    return longest





words = [
    "a",
    "b",
    "ba",
    "bca",
    "bda",
    "bdca"
]

longestChain(words)