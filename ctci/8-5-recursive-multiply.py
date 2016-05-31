"""
Write a recursive function to multiply two positive integers without using the * operator.
You can use addition, subtraction, and bit shifting, but you should minimize the number
of those operations.

a = 8
b = 9

sol_1 = 5 + 5
sol_2 = 2 + 2 + 2 + 2 + 2

[_, _, _, _]
[_, _, _, _]

"""

# Time complexity  O( log small )

def multiply(a, b):
	smaller = a if a < b else b
	bigger = b if b > a else a

	return helper(smaller, bigger)

def helper(smaller, bigger):
	print (smaller, bigger)
	if smaller == 0: return 0
	elif smaller == 1: return bigger

	# Divide by 2
	half_smaller = smaller >> 1

	# Lookup for the even division
	half_prod = helper(half_smaller, bigger)	
	
	# small + small + remaining(odd)
	if smaller % 2 == 0:
		return half_prod + half_prod

	else:
		return half_prod + half_prod + bigger



result = multiply(211313, 1500)
print (result)