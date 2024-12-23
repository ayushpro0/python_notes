""" Comples Data Structures """


""" 1. Dict with list as value """
empData =   {
                '1a':['ABC', 24, 25000],
                '2a':['xyz', 25, 35000]
            }

print("empData = ", empData, "type = ", type(empData))
# empData =  {'1a': ['ABC', 24, 25000], '2a': ['xyz', 25, 35000]} 
# type =  <class 'dict'>

print("Details of 1a = ", empData['1a'], " type of 1a value = ", type(empData['1a']))
# Details of 1a =  ['ABC', 24, 25000]  
# type of 1a value =  <class 'list'>

print("Name of empId 1a = ", empData['1a'][0]) # Name of empId 1a =  ABC

for k in empData:
    print("Details of empID ", k, " = ", empData[k])

# Details of empID  1a  =  ['ABC', 24, 25000]
# Details of empID  2a  =  ['xyz', 25, 35000]


print("-----------------------------------------------------")

# nested loop to traverse over the inner list 1 by 1

for k in empData:
    print("Details of empID ", k, " : ")
    for i in empData[k]:
        print("\t", i)

# Details of empID  1a  :
#          ABC
#          24
#          25000
# Details of empID  2a  :
#          xyz
#          25
#          35000


print("------------------------------------")

# increase the sal of every emp by 10000
for k in empData:
    print("Details of empID ", k, " : ")
    for i in range(len(empData[k])):
        if i == 0: print("\tName = ", empData[k][i])
        if i == 1: print("\tAge = ", empData[k][i])
        if i == 2:
            print("\tSal = ", empData[k][i])
            empData[k][i] += 10000;

print("------------------------------------")
# print the slab again to check if the values are increase or not
for k in empData:
    print("Details of Updated empID ", k, " : ")
    for i in range(len(empData[k])):
        if i == 0: print("\tName = ", empData[k][i])
        if i == 1: print("\tAge = ", empData[k][i])
        if i == 2:
            print("\tSal = ", empData[k][i])

print("------------------------------------")

""" 2. Dict with dict as value """

empData = {
                '1a': {"Name":"ABC", "Age":24, "Sal":25000},
                'a': {"Name":"xyz", "Age":35, "Sal":35000}
           }

print("empData = ", empData, " type = ", type(empData))
print("Details of 1a = ", empData['1a'], type(empData["1a"]))
# Details of 1a =  {'Name': 'ABC', 'Age': 24, 'Sal': 25000} 
# <class 'dict'>

print("Name of empID 1a = ", empData['1a']["Name"])


for k in empData:
    print("Details of empID ", k, " = ", empData[k])

print("-------------------------------------------")

# nested loop to traverse over the inner dict 1 by 1:

for k in empData:
    print("Details of empID ", k, " : ")
    for k1 in empData[k]:
        print("\t", k1, " = ", empData[k][k1]) 
        if k1 == "Sal" : 
            empData[k][k1] += 10000

print("--------------------------------------------")

#increased the sal of every emp by 10000
print("empData = ", empData)