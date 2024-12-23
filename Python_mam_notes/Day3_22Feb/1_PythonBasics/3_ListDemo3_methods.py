"""
List / tuple def, slicing
"""
# list def
list1 = [10, 20, 30, 40]
print("list1 = ", list1, " Type = ", type(list1), " ID = ", id(list1))
# list1 =  [10, 20, 30, 40]  Type =  <class 'list'>  ID =  4487789376

list1.append(50)
print("list1 = ", list1, " Type = ", type(list1), " ID = ", id(list1))
# list1 =  [10, 20, 30, 40, 50]  Type =  <class 'list'>  ID =  4487789376

list1.append([55, 66])  # adds list as 1 object inside list1
list1.extend([99, 88])  # adds 99 and 88 as separate elements
print("list1 = ", list1, " Type = ", type(list1), " ID = ", id(list1))
# list1 =  [10, 20, 30, 40, 50, [55, 66], 99, 88]  Type =  <class 'list'>  ID =  4487789376

print("---------------------------------------------------------------------")

list2 = [99, 88, 10, 33, 555, 345, 199, 56789]
print("list2 = ", list2, " Type = ", type(list2), " ID = ", id(list2))
# list2 =  [99, 88, 10, 33, 555, 345, 199, 56789]  Type =  <class 'list'>  ID =  1529337771392

# sort() -> this sort function does the inplace sorting of the original list
list2.sort()
print("Ascending sorted list2 = ", list2, " ID = ", id(list2))
# Ascending sorted list2 =  [10, 33, 88, 99, 199, 345, 555, 56789]  ID =  1529337771392

list2.sort(reverse=True)
print("Descending sorted list2 = ", list2, " ID = ", id(list2))
# Descending sorted list2 =  [56789, 555, 345, 199, 99, 88, 33, 10]  Type =  <class 'list'>  ID =  1529337771392

print("---------------------------------------------------------------------")

words = ["xyz", "abc", "bob", "lmn"]
print("Original words = ", words, " Type = ", type(words), " ID = ", id(words))
# Original words =  ['xyz', 'abc', 'bob', 'lmn']  Type =  <class 'list'>  ID =  1529337866240

words.sort()
print("Ascending sorted words = ", words, " Type = ", type(words), " ID = ", id(words))
# Ascending sorted words =  ['abc', 'bob', 'lmn', 'xyz']  Type =  <class 'list'>  ID =  1529337866240


# list2 = [99,88,10,33,555,"abc",345,199,56789]
# list2.sort()#TypeError: '<' not supported between instances of 'str' and 'int'


# list.reverse
# list.pop
# list.insert

