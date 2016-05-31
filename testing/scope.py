class memoized(object):
	def __init__(self, func):
		self.func = func
		self.cache = {}

	def __call__(self, *args):
		if args in self.cache:
			return self.cache[args]
		else:
			value = self.func(*args)
			self.cache[args] = value
			return value 

@memoized
def fibonacci(n):
	if n in (0, 1):
		return n

	return fibonacci(n - 1) + fibonacci(n - 2)







class Coordinate(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "Coord: " + str(self.__dict__)


one = Coordinate(100, 300)
print (one)


def say_hi(cum):
	print ("HELLO WORLD")
	return cum



def outer_dec(some_func, cum):
	def inner_dec():
		print ("Start dec")
		res = say_hi(cum)

		return res + 10

	return inner_dec

decorated = outer_dec(say_hi, 20)
resp = decorated()
print (resp)



"""
def outer(x):
	
	def inner():
		print (x + 1)

	return inner


print_outer1 = outer(1)
print_outer2 = outer(10)
print_outer1()
print_outer2()


def add(x, y):
	return x + y


def apply_func(func, x, y):
	return func(x, y)


resp = apply_func(add, 1, 2)
print (resp)


"""