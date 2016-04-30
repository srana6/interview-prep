"""
Imagine you have a collection of N wines placed next to each other on a shelf. For simplicity, let's number the wines 
from left to right as they are standing on the shelf with integers from 1 to N, respectively. The price of the i-th wine 
is pi (prices of different wines can be different). 

Because the wines get better every year, supposing today is the year 1, on year y the price of the i-th wine will 
be y*pi, i.e. y-times the value that current year.

You want to sell all the wines you have, but you want to sell exactly one wine per year, starting on this year. One 
more constraint - on each year you are allowed to sell only either the leftmost or the rightmost wine on the shelf 
and you are not allowed to reorder the wines on the shelf (i.e. they must stay in the same order as they are in the 
beginning).

You want to find out, what is the maximum profit you can get, if you sell the wines in optimal order.

So for example, if the prices of the wines are (in the order as they are placed on the shelf, from left to right): 

p1=1, p2=4, p3=2, p4=3

The optimal solution would be to sell the wines in the order p1, p4, p3, p2 for a total profit 1*1 + 3*2 + 2*3 + 4*4 = 29



It runs O(N^2) time, because there are O(N^2) different arguments our function can be 
called with and for each of them, the function runs only once with O(1) time complexity.

"""



class Wines(object):	
	def __init__(self, wines):
		self.wines = wines
		self.memo = [[-1 for j in range(len(wines))] for i in range(len(wines))]

	def profit(self, start = 0, end = None):
		if end is None: 
			end = len(self.wines) - 1

		if start > end: 
			return 0

		year = len(self.wines) - (end - start + 1) + 1

		self.memo[start][end] = max( 	
			self.profit(start + 1, end) + year * self.wines[start], 
		 	self.profit(start, end - 1) + year * self.wines[end])
		
		return self.memo[start][end]

sol = Wines([2, 3, 5, 1, 4, 1, 2, 3, 4, 9, 1]).profit()
print (sol)
