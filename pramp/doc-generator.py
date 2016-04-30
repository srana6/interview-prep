from operator import itemgetter

def isLetter(character):
   return (ord(character) >= ord('a') and ord(character) <= ord('z'))

def word_engine(doc):
   table = {}
   n = len(doc)

   i = 0
   j = 0
   while i <= j and j < n:
      while i < n and not isLetter(doc[i]):
         i += 1
         j += 1

      while j < n and isLetter(doc[j]):
         j += 1

      if i < j and j < n:
         table[doc[i:j]] = table.get(doc[i:j], 1) + 1
         i = j
      j += 1

   return sorted(table.items(), key=itemgetter(1), reverse=True)

arr =  "practice makes perfect.    get perfect by practice. just practice!  131"
sol = word_engine(arr)

print (sol)


