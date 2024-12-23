# Example :Functions extend   reverse sort, +operator

listTwo = [123, 'abc', 4.56]  # List definition with different data objects, List is mutable
print('Original list = ', listTwo)  # Original list =  [123, 'abc', 4.56]

listTwo.reverse()  # reverse function to reverse a list -> inplace reverse - modifies the original data
print("reversed list listTwo =", listTwo)  # reversed list listTwo = [4.56, 'abc', 123]

print("------------------------------------------------------------")

listOne = [123, 'abc', 4.56]
listOne.extend([1, 2])
print("extended list = ", listOne)  # extended list =  [123, 'abc', 4.56, 1, 2]

print("------------------------------------------------------------")

print("in operator to check existence of abc element in listTwo = ", 'abc' in listTwo)  # True
print("not in operator to check existence of abc element in listTwo = ", 'abc' not in listTwo)  # False

print("------------------------------------------------------------")

number_list = [43, -1.23, -2]
string_list = ['hello', 'world']
print("Concatenation + operator creating new list = ", string_list + number_list)
# Concatenation + operator creating new list =  ['hello', 'world', 43, -1.23, -2]

print("------------------------------------------------------------")

listX = [10, 0, 44, [1, 9], [55, 77, 11], 100, 1000, 'a', 'z']
print("Original X list = ", listX)
# Original X list =  [10, 0, 44, [1, 9], [55, 77, 11], 100, 1000, 'a', 'z']

# listX.sort() #TypeError: '<' not supported between instances of 'list' and 'int'
# print ("Sorted X list = ",listX)

print("------------------------------------------------------------")

# sorted(list) function -> return the sorted list -> does not modify the original data
l1 = [23, 10, 6, 99]
sortlist1 = sorted(l1)
print("Original list l1 = ", l1)  # (23, 10, 6, 99)
print("Sorted list Ascending = ", sortlist1)  # [6, 10, 23, 99]

sortlist2 = sorted(l1, reverse=True)  # this is called as keyworded argument passing
print("Sorted list Descending = ", sortlist2)  # [99, 23, 10, 6]
