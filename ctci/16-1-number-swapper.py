"""
Write a function to swap a number in place

That is, without temporary variables
"""

def swap(a, b):
	a = a + b
	b = a - b
	a = a - b

	return (a, b)



print (swap(-10, 2999))