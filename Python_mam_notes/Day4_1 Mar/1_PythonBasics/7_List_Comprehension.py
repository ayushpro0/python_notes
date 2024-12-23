import math

# List Comprehension

listOne = [1, 2, 3, -5, -10]

# conventional for loop code
new_listOne = []

for i in listOne:
    new_listOne.append(i * 2)

print("Original list = ", listOne)  # [1, 2, 3, -5, -10]
print("Updated new list = ", new_listOne)  # [2, 4, 6, -10, -20]

# OR

new_listOne1 = [x * 2 for x in listOne]  # list comprehension
print("Updated new list = ", new_listOne1)  # [2, 4, 6, -10, -20]

# comprehension to operate on every element
print("list one =", listOne)  # [1, 2, 3, -5, -10]
print("new list =", new_listOne)  # [2, 4, 6, -10, -20]

str = "abc"
print(str.upper())  # returns upper case string

words = ["abc", "xyz", "lmn", "aaaa", "bbb"]
upperwords = [i.upper() for i in words]
print("Original words = ", words)  # ['abc', 'xyz', 'lmn', 'aaaa', 'bbb']
print("Upper words =", upperwords)  # ['ABC', 'XYZ', 'LMN', 'AAAA', 'BBB']

print("-------------------------------------------------")
square_list = [x ** 2 for x in listOne]
print("Square list =", square_list)  # [1, 4, 9, 25, 100]

print("-------------------------------------------------")

print("math.sqrt(25) = ", math.sqrt(25))  # 5.0

square_root_list = [int(math.sqrt(x)) for x in square_list]
print("Square root elements = ", square_root_list)  # [1, 2, 3, 5, 10]

print("-------------------------------------------------")

# dictionary comprehension
list1 = [1, 2, 3, 4]  # it is  a list
dictionaryTwo = {x: x * x for x in list1}
print("dictionaryTwo = ", dictionaryTwo)  # {1: 1, 2: 4, 3: 9, 4: 16}
