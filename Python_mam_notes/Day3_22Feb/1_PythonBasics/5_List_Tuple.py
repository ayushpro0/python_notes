# List data tuple data Example

listOne = [123, 'abc', 4.56]  # List definition with different data objects, List is mutable

# listOne[5] = 500   #IndexError: list assignment index out of range

print("listOne = ", listOne)  # listOne =  [123, 'abc', 4.56]

# Tuple --->immutable
tupleOne = (123, 'abc', 4.56)  # Tuple definition with different data objects, Tuple is immutable
print("tupleOne = ", tupleOne)  # tupleOne =  (123, 'abc', 4.56)

print("-------------------------------------------------------------------")

print("First element of listOne = ", listOne[0])  # First element of listOne =  123
print("First element of tupleOne = ", tupleOne[0])  # First element of tupleOne =  123

print("slicing of listOne from index 0 up to 2 = ", listOne[0:2])
# slicing of listOne from index 0 upto 2 =  [123, 'abc']

print("-------------------------------------------------------------------")

# inner list
listTwo = [4.56, ['inner', 'list']]  # inner list defined
print("Inner listTwo = ", listTwo)  # Inner listTwo =  [4.56, ['inner', 'list']]

# inner list in a Tuple
tupleTwo = (123, 'abc', 4.56, ['inner', 'tuple'], 7 - 9j)
print("Tuple with inner List = ", tupleTwo)
# Tuple with inner List =  (123, 'abc', 4.56, ['inner', 'tuple'], (7-9j))

tupleTwo[3].append(100)
print("Tuple with inner List appended = ", tupleTwo)
# Tuple with inner List appended =  (123, 'abc', 4.56, ['inner', 'tuple', 100], (7-9j))

# Tuple with Inner Tuple
t2 = (10, 20, (1, 2, 3))
print("Tuple with inner tuple = ", t2)
# Tuple with inner tuple =  (10, 20, (1, 2, 3))

print("-------------------------------------------------------------------")

# List with inner list
listFour = [123, 'abc', 4.56, ['inner', 'list']]
listFour[1] = 200
# listFour[4]=999  # IndexError: list assignment index out of range

print("List listFour = ", listFour)  # List listFour =  [123, 200, 4.56, ['inner', 'list']]

print("3rd index element of ListFour = ", listFour[3])  # 3rd index element of istFour =  ['inner', 'list']

# print ("6th index inner list = ", listFour [6]) #run time error IndexError: list index out of range

print("first index element of inner list from listFour = ", listFour[3][0])
# first index element of inner list from listFour = inner

print("-------------------------------------------------------------------")

a = 12, 34, 5  # comma separated objects without any bracts defaults to tuple definition
print("Tuple a = ", a)  # Tuple a =  (12, 34, 5)
print("a = ", type(a))  # a = <class 'tuple'>

print("-------------------------------------------------------------------")
