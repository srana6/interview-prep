class Solution:
    
    # checks each bit to see if its ON or OFF
    def numSetBits(self, num):
        count = 0
        while num:
            if num & mask == 1:
                count += 1
            num = num >> mask
        
        return count


    # same as below without comments,  it just chekcs bits turned ON. Not extra work
    def numSetBits(self, num):        
        count = 0

        while num:
            num = num & (num - 1)
            count += 1        
        return count


    def numSetBits(self, num):        
        count = 0

        """
        
        100100000
        100011111
        100000000

        """

        while num:
            print ()

            # number so far
            print (bin(num))

            # turns off latest ON bit
            print (bin(num - 1))

            num = num & (num - 1)

            # with the AND operation, just the ones were ON before stay, so the count happens
            print (bin(num))
            count += 1
        
        return count


num = 299

sol = Solution().numSetBits(num)
print (sol)
            
