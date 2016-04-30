"""

Write a function to swap a number in place 
(that is, without temporary variables)

"""

from operator import xor

class Solution(object):
	def swap(self, a, b):		
		a = a - b
		b = b + a
		a = b - a
		return (a, b)