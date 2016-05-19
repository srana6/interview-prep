"""
Implement the 'cd' command i.e. given a function cd('a/b','c/../d/e/../f'), where 1st param is current 
directory and 2nd param is the sequence of operations, find the final directory that the user will be 
in when the cd command is executed
"""

from collections import deque

def cd(source, dest):	
	directory = source.split('/')
	stack = deque(dest.split('/'))

	while stack:
		elem = stack.popleft()
		if elem == '..' and directory:
			directory.pop()
		else:
			directory.append(elem)

	return "/".join(directory)


result = cd('a/b','c/../d/e/../f')
print (result)


