# Dictionary Def

colors = {'red':255, 'blue':100, 'yellow':150, 'red': 11}
print("Colors dict = ", colors) # unordered
# Colors dict =  {'red': 11, 'blue': 100, 'yellow': 150}

print("Value of red = ", colors['red']) # Value of red =  11

colors['yellow'] = 99  # value of 'yellow' key will be updated

# key value pair will be created if it is not already present
colors['magenta'] = 55

print("Updated colors dict = ", colors)
# Updated colors dict =  {'red': 11, 'blue': 100, 'yellow': 99, 'magenta': 55}

print("------------------------------------------------------------")

k = colors.keys()
print("Keys = ", k, "type of k = ", type(k))
# Keys =  dict_keys(['red', 'blue', 'yellow', 'magenta']) 
# type of k =  <class 'dict_keys'>

v = colors.values()
print("values of k = ", v, "type of v = ", type(v))
# values of k =  dict_values([11, 100, 99, 55]) 
# type of v =  <class 'dict_values'>

colors_items = colors.items()
print("Color Pairs = ", colors_items, "type of color pairs = ", type(colors_items))
# Color Pairs =  dict_items([('red', 11), ('blue', 100), ('yellow', 99), ('magenta', 55)]) 
# type of color pairs =  <class 'dict_items'>

print("----------------------------------------------------")

print("Red Exists ? = ", 'red' in colors ) # Red Exists ? =  True

l1 = list(k) # converting keys of colors dictionary into list
l1.sort()

print("Sorted list of keys = ", l1) 
# Sorted list of keys =  ['blue', 'magenta', 'red', 'yellow']

print("----------------------------------------------------")

# printing the dictionary
for i in l1:
    print("Key = ", i, "\t Value = ", colors[i])
    colors[i] += 10

print("----------------------------------------------------")

for i in l1:
    print("Key = ", i, "\t Value = ", colors[i])

print("----------------------------------------------------")

# dict.update

emp = {'1a':35000, '2a':45000}
data = {'3a':33000, '4a':44000}

emp.update(data)
print("Dict emp = ", emp, "ID = ", id(emp), "type = ", type(emp))
# Dict emp =  {'1a': 35000, '2a': 45000, '3a': 33000, '4a': 44000} 
# ID =  1881360527744 type =  <class 'dict'>

print("----------------------------------------------------")

# zip function

ids = ['1a', '2a']
sals = [25000, 35000]

newDict = dict(zip(ids, sals))
print("newDict = ", newDict, "ID = ", id(newDict), " type of newDict = ", type(newDict  ))
# newDict =  {'1a': 25000, '2a': 35000} 
# ID =  1664853076480  type of newDict =  <class 'dict'>

"""
Take emp data as a strnig from input with ID:sal, put that in dict
"""

# method1
emp = {}
id, sal = input("Enter ID:Sal = ").split(":")
emp[id] = sal

# method2
emp = dict(input("Enter emp name and salary : ").split() for _ in range(2))