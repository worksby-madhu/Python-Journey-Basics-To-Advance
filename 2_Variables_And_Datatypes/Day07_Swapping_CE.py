a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))

#with temp
temp=a
a=b
b=temp
print(a,b)

#without temp
a,b=b,a
print(a,b)

#using addition/subtraction
a=a+b
b=a-b
a=a-b
print(a,b)
