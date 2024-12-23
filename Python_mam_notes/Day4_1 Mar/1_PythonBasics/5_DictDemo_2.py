"""Dictionary Def"""

colors = {'red': 255, 'blue': 100, 'yellow': 150, 'red': 11}

print("Colors dict = ", colors)  # unordered

print("Value of red =", colors['red'])  # 11

colors['yellow'] = 99
colors['magenta'] = 55
print("Updated Colors  dict = ", colors)  # unordered

k = colors.keys()
v = colors.values()

print("Keys = ", k, "type of k = ", type(k))
# dict_keys(['red', 'blue', 'yellow', 'magenta'])  type of k =  <class 'dict_keys'>

print("Values = ", v, type(v))
# dict_values([11, 100, 99, 55]) <class 'dict_values'>

print("Colors pairs = ", colors.items(), type(colors.items()))  # <class 'dict_items'>
# dict_items[('blue', 100), ('magenta', 55), ('yellow', 99), ('red', 11)]

print("red exists ? = ", 'red' in colors)  # True

l1 = list(k)
l1.sort()
print("Sorted list of keys = ", l1)

print("------------------------------------------------")

for i in l1:
    print("Key = ", i, " | Value = ", colors[i])
    colors[i] += 10

print("------------------------------------------------")
for i in colors:
    print("Key = ", i, " | Value = ", colors[i])

print("------------------------------------------------")

# dict.update
emp = {'1a': 35000, '2a': 45000}
data = {'3a': 33000, '4a': 44000}

emp.update(data)

print("Dict emp = ", emp, "ID = ", id(emp), "type = ", type(emp))

ids = ['1a', '2a']
sals = [25000, 35000]
newDict = dict(zip(ids, sals))
print("newDict  = ", newDict, "ID = ", id(newDict), "type = ", type(newDict))
# newDict  =  {'1a': 25000, '2a': 35000} ID =  4502523136 type =  <class 'dict'>
