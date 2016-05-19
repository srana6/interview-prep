"""
Design a method to find the frequency of ocurrences of any given word in a book
What if we were running this algorithm multiple times?
"""

class InvalidBook(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)


class Solution(object):
	memo = {}

	def __init__(self, book):
		try:
			if book:
				lwords = book.split()
				for item in lwords:
					item = item.lower().strip()			
					self.memo[item] = self.memo.get(item, 0) + 1
			else:
				raise InvalidBook('Invalid Book')

		except InvalidBook as e:
			print ('Exception ocurred:', e.value)

		finally:
			print ('Bye')


	def word_frecuency(self, word):
		if word:
			return self.memo.get(word.lower(), 0)
		return 0

book = "\
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc maximus lectus vitae lacus efficitur, eget mattis quam consequat. Proin felis sem, tristique sit amet risus sit amet, faucibus viverra ipsum. Maecenas sollicitudin erat sollicitudin ornare vulputate. Integer diam lectus, porttitor sodales libero posuere, tristique scelerisque arcu. Vivamus sed imperdiet justo. Aenean iaculis felis sit amet dapibus euismod. Phasellus ullamcorper turpis eu lectus iaculis, nec vehicula mauris venenatis. Etiam nulla enim, lacinia ut accumsan ullamcorper, ultricies non est. Phasellus malesuada eros vestibulum fringilla maximus.\
\
Sed sit amet condimentum lectus. Aenean vitae orci tincidunt, mattis orci eget, viverra est. Ut ullamcorper auctor ex, non tincidunt tellus placerat eget. Quisque sodales arcu ac turpis suscipit aliquet et sed massa. Etiam pharetra magna id libero molestie fermentum. Donec at neque vel elit luctus iaculis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent imperdiet at nibh vel mollis. Sed ipsum metus, gravida fringilla pharetra at, iaculis dictum metus. Sed a interdum urna.\
\
Etiam in lacus nec eros vestibulum ultricies. Nam sollicitudin maximus enim, ac cursus sem cursus a. Curabitur vel elementum velit. Duis scelerisque est at purus dapibus suscipit. Nam commodo est nec mauris porttitor, vel hendrerit mauris auctor. Integer nulla dui, laoreet id dictum quis, fermentum ac lorem. Interdum et malesuada fames ac ante ipsum primis in faucibus. Fusce viverra pellentesque ligula. Donec lacinia risus risus, non viverra dui malesuada ac. Proin id dolor vel magna vehicula ultricies quis at metus. Donec a eleifend erat. Curabitur ac auctor diam. Ut semper augue sit amet iaculis suscipit. Aenean nibh nisl, tincidunt vitae enim ut, porttitor imperdiet elit. Quisque sit amet lectus vel purus ullamcorper ornare."

word = "sit"


finder = Solution(None)
found = finder.word_frecuency(word)
print(found)