"""
Design a method to find the frequency of ocurrences of any given word in a book.
What if we were running this algorithm multiple times?
"""

from collections import defaultdict

class Book(object):
	def __init__(self, book):
		self.book = book
		self.word_cache = defaultdict(int)

		compute_word_frequency()

	def compute_word_frequency(self):
		for elem in self.book:
			word = elem.strip().lower()
			if word:
				self.word_cache[elem] += 1


	def get_word_frequency(self, word):
		word = word.lower()
		if word in self.word_cache:
			return self.word_cache[word]
		return 0
