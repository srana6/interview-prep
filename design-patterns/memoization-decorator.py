import functools

# Class approach
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



# Function approach
def memoize(obj):
	cache = obj.cache = {}

	@functools.wraps(obj)
	def memoizer(*args, **kwargs):
		if args not in cache:
			cache[args] = obj(*args, **kwargs)
		return cache[args]

	return memoizer


#@memoized
@memoize
def fibonacci(n):
	if n in (0, 1):
		return n
	return fibonacci(n - 1) + fibonacci(n - 2)


print (fibonacci(50))