"""
String multiplication

aaaa3x[bbac2x[gg3x[pp]2x[ma]]]hh

aaa3x[cd]b

Result:
aaaabbacggppppppmamaggppppppmamabbacggppppppmamaggppppppmamabbacggppppppmamaggppppppmamahh

"""

def _multiply(string, start = 0):
	if not string: return ""
	buff = []
	size = len(string)	
	i = start
	j = start

	while j < size:			
		if string[j] == '[':
			k = j - 2
			while string[k - 1] >= '0' and string[k - 1] <= '9':
				k -= 1

			if i != k:
				buff.append(string[i:k])

			multiplier = int(string[k: j - 1])
			value, end = _multiply(string, j + 1)	
			buff.append(multiplier * value)

			i = end
			j = end

		elif string[j] == ']':			
			break

		else:
			j += 1

	
	buff.append(string[i:j])

	return ("".join(buff), j + 1)



def multiply(string):	
	res, end = _multiply(string)
	print (res)
	return res


string = "aaaa3x[bbac2x[gg3x[pp]2x[ma]]]hh"

multiply(string)