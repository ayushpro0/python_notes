"""
Dict Comprehension
"""

list1 = [1, 2, 3, 4]
newDict = {i: i ** 2 for i in list1}
print("list1 = ", list1)  # list1 =  [1, 2, 3, 4]
print("newDict = ", newDict)  # newDict =  {1: 1, 2: 4, 3: 9, 4: 16}

print("-----------------------------------------------")

empData = {'1a': 55000, '2a': 125000, '3a': 45000, '4a': 145000}
print("Original EmpData = ", empData)
# Original EmpData =  {'1a': 55000, '2a': 125000, '3a': 45000, '4a': 145000}

newEmpData = {}  # get the empData with sal > 100000
# method1
newEmpData = {k: empData[k] for k in empData if empData[k] > 100000}
print("newEmpData = ", newEmpData)  # newEmpData =  {'2a': 125000, '4a': 145000}

print("-----------------------------------------------")
