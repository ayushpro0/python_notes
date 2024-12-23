"""
List / tuple def, slicing
"""
# list def
list1 = [123, "abc", 3.145, 999]

print("list1 = ", list1, " Type = ", type(list1), " ID = ", id(list1))
# [123, 'abc', 3.145, 999]  Type =  <class 'list'>  ID =  1966481495232

print("list1[0] = ", list1[0], "type(list1[0])= ", type(list1[0]))
# list1[0] =  123 type(list1[0])=  <class 'int'>

print("list1[-1] = ", list1[-1])  # list1[-1] =  999

print("list1[1:3] = ", list1[1:3])  # list1[1:3] =  ['abc', 3.145]

# print(list1[5]) #IndexError: list index out of range

print("list1[1:] = ", list1[1:])  # ['abc', 3.145, 999]
print("list1[:3] = ", list1[:3])  # [123, 'abc', 3.145]

print("---------------------------------------------------------------------")

list1[-1] = 1000  # updating a single element
print("list1 = ", list1, " Type = ", type(list1), " ID = ", id(list1))
# list1 =  [123, 'abc', 3.145, 1000]  Type =  <class 'list'>  ID =  1966481495232

print("----------------------------------------------------------------------")

# tuple def
tup1 = (123, "abc", 3.145, 999)
print("tup1 = ", tup1, " Type = ", type(tup1), " ID = ", id(tup1))
# tup1 =  (123, 'abc', 3.145, 999)  Type =  <class 'tuple'>  ID =  1287908895584

print("tup1[0] = ", tup1[0], "type(tup1[0])= ", type(tup1[0]))
# tup1[0] =  123 type(tup1[0])=  <class 'int'> 

print("tup1[-1] = ", tup1[-1])  # tup1[-1] =  999
print("tup1[1:3] = ", tup1[1:3])  # tup1[1:3] =  ('abc', 3.145)

# print(tup1[5])#IndexError: list index out of range

print("tup1[1:] = ", tup1[1:])  # ['abc', 3.145, 999]
print("tup1[:3] = ", tup1[:3])  # [123, 'abc', 3.145]

# tup1[0] = 100 # this won't work because Tuple is Non Mutable
# print("tup1 = ", tup1, " Type = ", type(tup1), " ID = ", id(tup1))
# TypeError: 'tuple' object does not support item assignment

print("----------------------------------------------------------------------")

t1 = 10, 20, 30, 30, 30  # comma separated values defaults to Tuple
print("t1 = ", t1, " Type = ", type(t1), " ID = ", id(t1))
# t1 =  (10, 20, 30)  Type =  <class 'tuple'>  ID =  4458935680

# t1[0] = 100 # TypeError: 'tuple' object does not support item assignment

# Tuple Methods - count, index

ans = t1.count(30)
print("30 count in t1 = ", ans)  # 30 count in t1 =  3

ind = t1.index(20)
print("Index of 20 in t1 = ", ind)  # Index of 20 in t1 =  1

# ind = t1.index(202020)
# print("Index of 202020 in t1 = ", ind) # ValueError: tuple.index(x): x not in tuple

print("END!!!")
