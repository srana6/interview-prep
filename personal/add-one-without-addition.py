"""
Bitwise Operation, Add one to a number without using + 
"""

def inc(n):	
	# if rightmost bit is on, turn it off and turn on next off from left side
	if n & 1:
		return inc(n >> 1) << 1

	# turn on rightmost bit
	return n | 1



for i in range(100):
	assert i + 1 == inc(i)


