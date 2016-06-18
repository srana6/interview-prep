"""

Questions:


What is a typical workday like?

How much importance do you guys give to innovation specially coming from junior people in the team?

What is the best aspect of working for Two Sigma? What is the most challenging?

What is your favorite part?


"""


import unittest


class Test(unittest.TestCase):
	def test_something(self):
		for (change, expected) in self.data:			
			self.assertEqual(_a_, _exp_)


unittest.main()







"""

# 4 + 5 = 9

# “4 5 + ” represents 4 + 5, 
# “4 5 + 1 - “ represents “4 + 5 - 1”
# + -  
# x  op  y  -> (  x  y op  )  z  op 


PolishNotation


Operand 
    Integer

Operand  <Operator>  Operand


Operator 
    operator

    Addition
        +  -  * 
    Substraction



    
stack ->  18
op ->  
result = 18

x + y
x - y
x / y
x * /
x .. /

4 5 + 1 - 10 +

"""

class Operand(object):



class Operator(object):
    def perform_operation(operand_a, operand_b):
        pass
        
    
class Addition(Operator):
    
    
    
class Substraction(Operator):

    

class PolishNotationCalculator(object):
    def __init__(self):
        self.stack = []
        
    def executeInput(self, string):
        if not string: return 0
        size = len(string)
        lstring = string.split()
        
        for i in range(size):
            value = lstring[i]
            
            # number
            if value >= '0' and value <='9':
                self.stack.push(value)
                
            else:
                if len(self.stack) >= 2:
                    a, b = self.stack.pop(), self.stack.pop()
                    
                    if value == '+':
                        result = a + b
                        
                    self.stack.push(result)
                
                else:
                    # invalid
                    pass
                
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
