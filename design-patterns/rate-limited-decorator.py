import time
import threading


class rateLimited(object):
	def __init__(self, rate):		
		self.rate = rate
		self.interval = 1.0 / float(rate)
		self.last_time_called = 0.0
		self.lock = threading.Lock()

	def __call__(self, func):		
		def wrapped_func(*args, **kwargs):
			self.lock.acquire()

			elapsed = time.clock() - self.last_time_called
			left_to_wait = self.interval - elapsed

			if left_to_wait > 0:
				time.sleep(left_to_wait)

			self.lock.release()

			value = func(*args, **kwargs)

			self.last_time_called = time.clock()
			return value
		
		return wrapped_func


@rateLimited(4)
def callAPI(name, lastname):
	print ("Hello %s %s" % (name, lastname))
	

for i in range(10):
	callAPI("jose", "castillo")
