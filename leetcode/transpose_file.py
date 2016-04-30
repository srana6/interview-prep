
class Solution(object):
    def transpose_file(self, filename):
        array = []
        header = []
        transpose = []

        with open(filename) as f:
            header = f.readline().strip().split(' ')
            for column in header:
                transpose.append([column])


            row = 1
            for i, line in enumerate(f):
                line_arr = line.strip().split(' ')
                for j, element in enumerate (line_arr):
                    transpose[j].append(element)

        for i in range(0, len(transpose)):
            print (' '.join(transpose[i]))

        


            
sol = Solution()
sol.transpose_file('file.txt')
#sol.transpose_file('transpose_file.txt')

