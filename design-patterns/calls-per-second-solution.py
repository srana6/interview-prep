import time, threading

def rate_limited(max_per_second):
	'''
	Decorator that make functions not be called faster than
	'''

	lock = threading.Lock()
	minInterval = 1.0 / float(max_per_second)

	def decorate(func):
		lastTimeCalled = [0.0]

		def rateLimitedFunction(args,*kargs):
			lock.acquire()
			elapsed = time.clock() - lastTimeCalled[0]

			leftToWait = minInterval - elapsed

			if leftToWait > 0:
				time.sleep(leftToWait)

			lock.release()

			ret = func(args,*kargs)
			lastTimeCalled[0] = time.clock()
			return ret
		return rateLimitedFunction
	return decorate



@rate_limited(2)  # 2 per second at most
def PrintNumber(num):
	print (num)

if __name__ == "__main__":
	print ("This should print 1,2,3... at about 2 per second.")
	for i in range(1,10):
		PrintNumber(i)