"""Dictionary Def"""

colors = {'red': 255, 'blue': 100, 'yellow': 150, 'red': 11}
print("Colors dict = ", colors)  # unordered

print("Value of red  =", colors['red'])  # 255

colors['yellow'] = 99  # key value pair will be craeted
colors['magenta'] = 55
print("Updated Colors  dict = ", colors)  # unordered
k = colors.keys()
v = colors.values()
print("Keys = ", k, "type of k = ", type(k))
# dict_keys(['red', 'blue', 'yellow', 'magenta'])  tyep of k =  <class 'dict_keys'>
print("Values = ", v)  # dict_values([11, 100, 99, 55])
print("red exists ? = ", 'red' in colors)  # True
print("Colors pairs = \n", colors.items())  # [('blue', 100), ('magenta', 55), ('yellow', 99), ('red', 11)]
l1 = list(k)
l1.sort()
print("Sorted list of keys = ", l1)
for i in l1:
    print("Key = ", i, "Value = ", colors[i])
    colors[i] += 10

print("------------------------------------------------")
for i in colors:
    print("Key = ", i, "Value = ", colors[i])
# dict.update

print("------------------------------------------------")
emp = {'1a': 35000, '2a': 45000}
data = {'3a': 33000, '4a': 44000}
emp.update(data)
print("Dict emp = ", emp, "ID = ", id(emp), "type = ", type(emp))

ids = ['1a', '2a']
sals = [25000, 35000]
newDict = dict(zip(ids, sals))
print("newDict  = ", newDict, "ID = ", id(newDict), "type = ", type(newDict))
# newDict  =  {'1a': 25000, '2a': 35000} ID =  4502523136 type =  <class 'dict'>


"""
In memory Data storage decision: str, list, tuple, dict
Take emp data as as a string from input with ID:sal, put that in dict
"""
emp = {}
d, sal = input("EnterID:Sal -").split(':')

emp[id] = sal

employees = dict(input("Enter emp name and salary : ").split() for _ in range(2))

keys = []
values = []
myDict = {k: v for (k, v) in zip(keys, values)}
