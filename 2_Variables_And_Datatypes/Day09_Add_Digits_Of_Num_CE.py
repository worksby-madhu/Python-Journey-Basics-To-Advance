num=input("Enter a two digits num:") #Enter a two digits num:47
num_1= num[0]
num_2= num[1]
''' accessing'''
print(num_1+num_2) #47
'''num_1 and num_2 are strings so we need to use type conversion here to add the digits'''
print(int(num_1)+int(num_2)) #11 