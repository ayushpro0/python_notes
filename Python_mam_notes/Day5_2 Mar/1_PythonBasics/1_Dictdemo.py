"""
Dictionary: Mutable
Key:Value
key : unique : Immutable : int, float, str, tuple
Value :anything : int, float, str, tuple, list, set, dict

"""
empData = {}
print("empData  = ", empData, " type = ", type(empData), " ID = ", id(empData))
# empData  =  {}  type =  <class 'dict'>  ID =  4476518912


empData = {'1a': 25000, '2a': 35000}
print("empData  = ", empData, " type = ", type(empData), " ID = ", id(empData))

print("Sal of 1a empID = ", empData['1a'])  # 25000
empData['1a'] += 5000

print("empData  = ", empData, " type = ", type(empData), " ID = ", id(empData))
# print(empData[0])#KeyError: 0

for i in empData:
    print("emp ID :", i, " Sal = ", empData[i])
