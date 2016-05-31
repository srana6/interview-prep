"""
68. Text Justification


Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

"""
class Solution(object):	
	def buildLine(self, words, i, j, maxWidth, spacing):
		spaces = (j - i) - 1
		space_left = maxWidth - (spacing + spaces)

		if spaces == 0:
			return "".join(words[i:j] + ([" "] * space_left))

		extra_space = 0
		if space_left < maxWidth:
			extra_space = space_left // spaces + 1
		
		k = i
		while extra_space * spaces + spacing < maxWidth:
			words[k] = words[k] + " "
			k += 1
			spacing += 1

		return (" " * extra_space).join(words[i:j])


	def buildLastLine(self, words, i, j, maxWidth, spacing):
		line = " ".join(words[i:j])
		spacing_left = maxWidth - len(line)
		extra_space = " " * spacing_left
		new_line = [line, extra_space]

		return "".join(new_line)

	def doesFit(self, words, i, j,  maxWidth, spacing):
		offset = j - i
		temp_spacing = spacing + len(words[j]) + offset
		if temp_spacing <= maxWidth:
			return True
		return False

	def fullJustify(self, words, maxWidth):
		if not words or maxWidth <= 0: return [""]
		justified = []
		n = len(words)

		i = 0
		j = 0
		spacing = -1

		while j < n and spacing != 0:
			spacing = 0
			i = j

			while j < n:
				if self.doesFit(words, i, j, maxWidth, spacing):
					spacing += len(words[j])
					j += 1					
				else:
					break

			if j == n:
				new_line = self.buildLastLine(words, i, j, maxWidth, spacing)
			else:
				new_line = self.buildLine(words, i, j, maxWidth, spacing)
				
			justified.append(new_line)

		return justified



words = ["Here","is","an","example","of","text","justification."]
L = 16

lines = Solution().fullJustify(words, L)

for line in lines:
	print (line, len(line))