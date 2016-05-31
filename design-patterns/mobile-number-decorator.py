"""
Let's dive into decorators! You are given  mobile numbers. Sort them in ascending order then print them in the standard format shown below:


+91 xxxxx xxxxx

The given mobile numbers may have ,  or  written before the actual  digit number. Alternatively, there may not be any prefix at all. 

Input Format

The first line of input contains an integer , the number of mobile phone numbers. 
 lines follow each containing a mobile number.

Output Format

Print  mobile numbers on separate lines in the required format.

Sample Input

3
07895462130
919875641230
9195969878
Sample Output

+91 78954 62130
+91 91959 69878
+91 98756 41230


"""




def phone_type(func):
    def sort_phone_type(numbers):        
        for i, num in enumerate(numbers):
            snumber = str(num)
            size = len(snumber)
            numbers[i] = "+91 %s %s" % (snumber[size - 10: size - 5], snumber[size - 5:])            
        func(numbers)        
    return sort_phone_type

@phone_type
def sort_and_transform(numbers):
    numbers.sort()  

n = int(input())
numbers = [input() for number in range(n)]

sort_and_transform(numbers)

for num in numbers:
    print (num)

