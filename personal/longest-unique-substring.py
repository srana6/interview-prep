"""
Length of the longest substring without repeating characters
"""

def longest_unique_substring(string):
	if not string: return 0
	CHARS = 256
	visited = [-1] * CHARS

	n = len(string)
	max_len = 0
	curr_len = 0

	for i in range(n):
		character = ord(string[i])
		prev_index = visited[character]

		if prev_index == -1 or (i - curr_len > prev_index):	
			curr_len += 1
		else:
			curr_len = i - prev_index

		visited[character] = i
		max_len = max(max_len, curr_len)
		
	return max_len


string = "GEEKSFORGEEK"
length = longest_unique_substring(string)

print (length)

