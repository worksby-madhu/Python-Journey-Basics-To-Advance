list1 = [10, 20, 30]
list2 = [10, 20, 30]
list3 = list1

print(list1 is list2)       # False → Different objects
print(list1 is list3)       # True → Same object

print(list1 is not list2)   # True
print(list1 is not list3)   # False

print(id(list1))            # 2087426285760
print(id(list2))            # 2087426434752
print(id(list3))            # 2087426285760

# Integer
a = 10
b = 10

print(a is b)               # True → Same object, because Python reuses small integer objects
print(a is not b)           # False

print(id(a))                # 140721698915528
print(id(b))                # 140721698915528

