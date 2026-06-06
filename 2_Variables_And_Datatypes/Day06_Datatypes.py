var_1=3
var_2=True 
a=12
b=2
var_4=a<b
var_5=12.3
var_6="string"

#list
marks = [90, 85, 70]
x=12
y=13
z=14

#tuples
names = x,y,z
age=(22,33,44,55)

#set
nums={1,2}

#dict
std={
    "name": "Ana",
    "age": 20
}
print(var_1) # 3
print(var_1+1) # 4, int and int can be concatenated
print(type(var_1 )) #<class 'int'>
print(type(var_2)) #<class 'bool'>
print(var_4) #false or true
print(type(var_4)) #<class 'bool'>
print(type(var_5)) #<class 'float'>
print(type(var_6)) #<class 'str'>
print(type(marks)) #<class 'list'>
print(type(names)) #<class 'tuple'>
print(age) #(22, 33, 44, 55)
print(type(age)) #<class 'tuple'>
print(type(nums)) #<class 'set'>
print(type(std)) #<class 'dict'>
print(0o123) # 83, octal o,hexa x,binary b

#print(var_1+'str') #TypeError: unsupported operand type(s) for +: 'int' and 'str'
#var_3=true #true/false gives.... NameError: name 'true' is not defined. Did you mean: 'True'?