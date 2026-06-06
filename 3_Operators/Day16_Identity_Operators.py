a=10
b=10

print(a is b)  #True
'''it returns true not because having same value but because both variables refer to the same object(same memory location or same unique id)'''
print(id(b))  #140721404540104
print(a==b)   #True
'''it returns true because having same values to both variables a and b'''