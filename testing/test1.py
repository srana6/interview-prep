def reverse(string):
	if not string: return ""
	return " ".join(reversed(string.strip().split()))



string = "It       is hot   "
sol = reverse(string)
print (sol)
