vmls=len("Subhadra")
print(vmls) #8
#print(len(123)) #TypeError: object of type 'int' has no len()
print(len("123")) #3
a=3112
#print(len(a)) #TypeError: object of type 'int' has no len()
b=str(a) 
"""explicittype conversion >>>converted int to str """
print(type(a)) #<class 'int'>
print(type(b)) #<class 'str'>
print(len(b)) #4
#print("Ur name is having "+len(vmls)+" characters") #TypeError: can only concatenate str (not "int") to str
print("Ur name is having "+str(vmls)+" characters") #Ur name is having 8 characters