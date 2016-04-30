a = 4
b = 7
x = lambda: a if 1 else b
lambda x: 'big' if x > 100 else 'small'
print (x())