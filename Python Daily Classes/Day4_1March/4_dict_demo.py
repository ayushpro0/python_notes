# Dictionary : Mutable
# Key:Value pair
# key -> unique : Immutable -> int, float, str, tuple
# value -> anything : int, float, str, tuple, list or anything

empData = {}
print("empData = ", empData, " type = ", type(empData), " id = ", id(empData))
# empData =  {}  type =  <class 'dict'>  id =  1546630614464

empData = {'1a':25000, '2a':35000}
print("empData = ", empData, " type = ", type(empData), " id = ", id(empData))
# empData =  {'1a': 25000, '2a': 35000}  type =  <class 'dict'>  id =  2080823013760

print("Salary of 1a empID = ", empData['1a']) # Salary of 1a empID =  25000

empData['1a'] += 5000
print("empData = ", empData, " type = ", type(empData), " id = ", id(empData))
# empData =  {'1a': 30000, '2a': 35000}  type =  <class 'dict'>  id =  2422023287168

# print(empData[0]) # KeyError: 0

for i in empData:
    print("emp ID : ", i, " Sal = ", empData[i])
"""
emp ID :  1a  Sal =  30000
emp ID :  2a  Sal =  35000
"""