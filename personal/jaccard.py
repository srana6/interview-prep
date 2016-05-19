from __future__ import division

class Jaccard:

	def  __init__(self,args,args_ii):
		self.args = self.tokenize(args)
		self.args_ii = self.tokenize(args_ii)

		print (self.args)
		print (self.args_ii)

	def intersect(self):
		return [i for i in self.args if i in self.args_ii]

	def union(self):
		return set(self.args + self.args_ii)

	def similarity(self):
		intersect = len(self.intersect())
		union = len(self.union())
		if intersect == None and union == None:
			return 1
		return intersect / union

	def distance(self):
		return 1 - self.similarity()

	def tokenize(self,item):
		item = item.lower()
		return item.split(" ")

jaccard = Jaccard("I am Sam","I am Sam, Sa is awesome. Sam is a genius")
similarity = jaccard.similarity()
print (similarity)