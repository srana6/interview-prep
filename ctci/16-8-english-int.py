"""
Given an integers, print an English phrase that describes the integer

	Samples:
		1234  One thousand two hundred thirty four

		0 - 99
		["", thousand, million, billion]

"""

class EnglishNumbers(object):

	smalls = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 
			  'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
	tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'nity']
	bigs = ['', 'thousand', 'million']
	hundred = 'hundred'
	negative = 'negative'

	def convert(self, number):
		result = []
		if number >= 100:
			result.append(self.smalls[number // 100])
			result.append(self.hundred)
			number = number % 100

		if number >= 20:
			result.append(self.tens[number // 10])
			number = number % 10
		elif number >= 10 and number <= 19:
			result.append(self.smalls[number])


		if number >= 1 and number <= 9:
			result.append(self.smalls[number])

		return " ".join(result)


	def convert_from_int(self, number):
		if number == 0: return self.smalls[0]
		if number < 0: return "negative " + self.convert_from_int(abs(number))

		chunks = []
		count = 0
		while number > 0:
			res = number % 1000
			chunks.append(res)
			number = number // 1000
			count += 1

		result = []
		for i in reversed(range(count)):
			result.append(self.convert(chunks[i]))
			result.append(self.bigs[i])
		
		return " ".join(result)

res = EnglishNumbers().convert_from_int(20)
print (res)




