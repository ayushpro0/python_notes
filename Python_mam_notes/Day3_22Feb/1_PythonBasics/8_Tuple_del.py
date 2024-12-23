"""Tuple example - immutable"""

tupleOne = (123, 'abc', 4.56)  # tuple definition tupleOne
tupleTwo = (789, 'def', 2.24)  # tuple definition tupleTwo
tupleThird = tupleOne[0], tupleTwo[1]
# Tuples are immutable which means they cannot be updated or change values of tuple values.
# But they allow to take portions of Tuples to create a new Tuple.


print("Count of 123 in tupleOne = ", tupleOne.count(123))  # 1

print("tupleOne = ", tupleOne)  # tupleOne =  (123, 'abc', 4.56)
print("tupleTwo = ", tupleTwo)  # tupleTwo =  (789, 'def', 2.24)
print("New tupleThird = ", tupleThird)  # New tupleThird =  (123, 'def')

del tupleThird
# Removing individual tuple elements is not possible
# though it is possible to delete an entire tuple with del function

# print tupleThird
# #run time error - after removing the tuple we cannot print it

print("--------------------------------------------")

t1 = (1, 2, 3)
print("Original Tuple = ", t1)  # (1, 2, 3)

l1 = list(t1)
print("Converted Tuple into List by list function = ", l1)  # [1, 2, 3]

l1.append([100, 200])
print("Appended list = ", l1)  # [1, 2, 3, [100, 200]]

print("--------------------------------------------")

newT1 = tuple(l1)
print("New tuple from tuple method = ", newT1)  # (1, 2, 3, [100, 200])

"""
len(list1)
id(listOne)
type(listOne)
del

"""
