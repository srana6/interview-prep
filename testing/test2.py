def mult(a, b):
	return a * b


def multiply(numbers, func):
	if not numbers: return 1
	elem = numbers[0]
	return func(elem, multiply(numbers[1:], func))

numbers = [3, 10, -2, 1, -3, -20, -10, -5]
sol = multiply(numbers, mult)

print (sol)

cum = 1
for i in range(len(numbers)):
	cum *= numbers[i]
print (cum)


print (" ".join(map(str, numbers)))

# 14400000