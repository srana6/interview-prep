"""
Given 0100101
Flip the bit from i to j so that you end up with the max number of 1
Print that max number

Example:

0100101

0111011
	where  	i = 2
			j = 6
"""

print (int("0111011", 2))

from itertools import *
from copy import deepcopy

def flip(bit, i):
	bits[i] = bits[i] ^ 1
	return bits

def to_number(bits):
	bits = list(map(str, bits))
	return int("".join(bits), 2)

def maximize(bits, i, j):
	if i > j: return to_number(bits)

	first = maximize(bits, i + 1, j)

	flip(bits, i)
	second = maximize(bits, i + 1, j)

	if second > first:
		return second
	else:
		flip(bits, i)
		return first

def maximizes(bits, i, j):
	maximize(bits, i, j)
	return bits

bits = [0,1,0,0,1,0,1]
i = 2
j = 6
sol = maximizes(bits, i, j)

print (sol)