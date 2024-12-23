"""
List / tuple def, slicing
"""

# list def

list1 = [123, "abc", 3.145, 999]
print("list1 = ", list1, " Type = ", type(list1), " ID = ", id(list1)) 
# list1 =  [123, 'abc', 3.145, 999]  Type =  <class 'list'>  ID =  2948179907776

print("list1[0] = ", list1[0], " Type = ", type(list1[0])) # list1[0] =  123 Type =  <class 'int'>

print("list1[-1] = ", list1[-1]) # list1[-1] =  999

print("list1[1:3] = ", list1[1:3]) # list1[1:3] =  ['abc', 3.145]
# print("list1[5] = ", list1[5]) # IndexError: list index out of range

print("list1[1:] = ", list1[1:]) # list1[1:] =  ['abc', 3.145, 999]

print("list1[:3] = ", list1[:3]) # list1[:3] =  [123, 'abc', 3.145]

# checking if List is mutable or Not
list1[-1] = 1000
print("list1 = ", list1, " Type = ", type(list1), " ID = ", id(list1)) 
# list1 =  [123, 'abc', 3.145, 1000]  Type =  <class 'list'>  ID =  2182121084096

print("--------------------------------------------------------------")

# tuple def

list1 = (123, "abc", 3.145, 999)
print("list1 = ", list1, " Type = ", type(list1), " ID = ", id(list1)) 
# list1 =  (123, 'abc', 3.145, 999)  Type =  <class 'tuple'>  ID =  2000911870496

print("list1[0] = ", list1[0], " Type = ", type(list1[0])) # list1[0] =  123 Type =  <class 'int'>

print("list1[-1] = ", list1[-1]) # list1[-1] =  999

print("list1[1:3] = ", list1[1:3]) # list1[1:3] =  ['abc', 3.145]
# print("list1[5] = ", list1[5]) # IndexError: list index out of range

print("list1[1:] = ", list1[1:]) # list1[1:] =  ['abc', 3.145, 999]

print("list1[:3] = ", list1[:3]) # list1[:3] =  [123, 'abc', 3.145]

print("--------------------------------------------------------------")

t1 = 10, 20, 30, 30, 30, 40, 30
print("t1 = ", t1, "Type = ", t1, type(t1), "ID = ", id(t1))
# t1 =  (10, 20, 30) Type =  (10, 20, 30) <class 'tuple'> ID =  1950260125312

# checking if Tuple t1 is mutable
# t1[0] = 100 # TypeError: 'tuple' object does not support item assignment

# Tuple Functions
ans = t1.count(30) # 30 count in t1 =  4
print("30 count in t1 = ", ans)

ind20 = t1.index(20)
ind30 = t1.index(30)
print("Index of 20 = ", ind20) # Index of 20 =  1
print("Index of 30 = ", ind30) # gives out the first index of the element -> Index of 30 =  2

# ind1 = t1.index(20202)
# print("Index of 20202 in t1 = ", ind1) # ValueError: tuple.index(x): x not in tuple


print("END!!!")