"""
Implement a method to perform basic string compression using the counts of repeated characters.
For example:
    the string aabcccccaaa would become a2b1c5a3

If the "compressed" string would not become smaller than the original string, your method
should return the original string.

You can assume the string has only uppercase and lowercase letters.
"""

def compression(string):
    size = len(string)
    comp = ""
    count = 0
    
    for i in range(size):
        count += 1
        if i + 1 >= size or string[i] != string[i + 1]:
            comp += string[i] + str(count)              
            count = 0

            if len(comp) > size: return string
    return comp




test = "aaabbcc"
print (compression(test))


