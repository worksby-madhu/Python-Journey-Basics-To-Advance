list1 = [10, 20, 30]
list2 = [10, 20, 30]
list3 = list1

print(list1 is list2)       # False Same object / same identity
print(list1 is list3)       # True Same value / content

print(list1 is not list2)   # True
print(list1 is not list3)   # False

print(id(list1))    #2087426285760
print(id(list2))    #2087426434752
print(id(list3))    #2087426285760
