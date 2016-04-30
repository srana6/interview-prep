"""
Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].

"""

# NOT SOLVED YET


class Solution(object):
	def swap(self, arr, i, j):
		arr[i], arr[j] = arr[j], arr[i]
		return arr

	def permute(self, perm, arr, start):
		if start == len(arr) - 1:
			perm.append(arr)
		else:
			for i in range(start, len(arr)):
				if i > 0 and arr[i - 1] == arr[i]:
					continue		

				self.swap(arr, start, i)
				self.permute(perm, arr, start + 1)
				self.swap(arr, start, i)

	def permuteUnique(self, arr):
		perm = []
		self.permute(perm, sorted(arr), 0)
		return perm

test = [1, 1, 2]
sol = Solution()
print ('sol', sol.permuteUnique(test))







"""
class Solution(object):
    def permuteUnique(self, num):
        if not num:
            return []
        return self.permute(sorted(num))

    def permute(self, num):
        print (num)
        if len(num) == 1:
            return [num]

        ret = []
        for i in range(len(num)):
            if i > 0 and num[i - 1] == num[i]:
                continue

            print ('for perm', num[:i] + num[i + 1:])

            perm = self.permute(num[:i] + num[i + 1:])

            print ('add', perm)

            for p in perm:
                ret += [ [num[i]] + p ]

        return ret

test = [1, 1, 2]
sol = Solution()
print ('sol', sol.permuteUnique(test))

"""