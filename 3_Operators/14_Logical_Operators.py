'''Logical operators'''
a,b,c=0,4,5
d=True
e=False
print(not a and e)
print(a and b)
print(b or c)
print(not a and e and c)
print(not a and e or c)
print(not e)
print(a or e)
print((b>4)==a or e)
print((b>4)==a and e)
print(d<b)

# not returns the opposite boolean value
# and returns True when both conditions are True
# or returns True when at least one condition is True
