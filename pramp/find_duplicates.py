
def find_duplicates(arr1, arr2):
   n = len(arr1)
   m = len(arr2)
   duplicates = []
   
   i, j = 0, 0
   while i < n and j < m:
      if arr1[i] == arr2[j]:
         duplicates.append(arr1[i])
         i += 1
         j += 1
         
      elif arr1[i] < arr2[j]:
         i += 1
      else: 
         j += 1
   
   return duplicates


arr1 = [1, 2, 3, 10, 15]
arr2 = [2, 10, 20]
sol = [2, 10]

# Brute force
# O(n * m)
# (1)

# Solution 3
# O(n + m)
# O(1)



# Solution 1: Hash map  
# O(s + 1)
# O(s) ->  O(s * l)


# Solution 2
# O(s lg l)
# (1)

