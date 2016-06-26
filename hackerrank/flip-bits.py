"""

Given a number N. Flip all bits in its binary representation.

"""

def binp(num):
	return bin(num)[2:]

def flip(number):
	s = binp(number)
	result = ''.join([str(int(c) ^ 1)for c in s])
	return int(result, 2)

num = 36
flip(num)