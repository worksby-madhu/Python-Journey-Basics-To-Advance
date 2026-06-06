str='Subhadra'

print('s' in str)
print('S'in str)
print('dra'in str)
print('ubha'not in str)

list=[1,2,3,-1,-2,-3,00]

print(1 in [1,2,3,-1,-2,-3,00])
print(-1 in list )
print(-1 in (-2,-3,0,-1))
print(0 in list)       #in python 0 and 00 are same
print( 00 in list)
print(0 not in list)
print(2-3 in list)