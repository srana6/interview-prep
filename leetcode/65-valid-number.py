"""
Valid Number

Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

"""




class Solution(object):
	def isNumber(self, string):
		if not string: return False
		string = string.strip()
		size = len(string)

		# use flags to control states and correctness
		numberSeen = False
		pointSeen = False
		eSeen = False


		for i in range(size):

			# number present
			if string[i] >= '0' and string[i] <= '9':
				numberSeen = True

			# decimal starts
			elif string[i] == '.':
				if eSeen or pointSeen:
					return False
				pointSeen = True				

			# scientific not
			elif string[i] == 'e':
				if eSeen or not numberSeen:
					return False
				eSeen = True
				numberSeen = False

			# positive or negative
			elif string[i] == '-' or string[i] == '+':
				if i != 0 and string[i - 1] != 'e':
					return False

			else:
				return False


		# special cases are considered within conditions
		# and return False if found
		return numberSeen