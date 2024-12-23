"""
Complex data structures
1. Dict with list as value
"""

empData = {
    '1a': ["ABC", 24, 25000],
    '2a': ["xyz", 25, 35000],
}
print("empData = ", empData, "type = ", type(empData))
print("Details of 1a = ", empData['1a'], type(empData['1a']))  # ["ABC", 24, 25000]
print("Name of empID 1a = ", empData['1a'][0])

for k in empData:
    print("Details of empid ", k, " = ", empData[k])

print("---------------------------------------------------------")

# nested loop to traverse over the inner list 1 by 1:

for k in empData:
    print("Details of empid ", k, " : ")
    for v in empData[k]:
        print("\t", v)  # changing v value here will not update inner list

print("---------------------------------------------------------")
# increase the sal of every emp by 10000

for k in empData:
    print("Details of empid ", k, " : ")
    for i in range(len(empData[k])):
        if i == 0:
            print("\tName = ", empData[k][i])
        if i == 1:
            print("\tAge = ", empData[k][i])
        if i == 2:
            print("\tSal = ", empData[k][i])
            empData[k][i] += 10000

print("---------------------------------------------------------")

print("empData = ", empData, "type = ", type(empData))

"""
for k in empData:
    print("Details of empid", k, "=", empData[k])
    print("ID of employee :", "=", k)
    print("Name of employee :", "=", empData[k][0])
    print("Age of employee :", "=", empData[k][1])
    print("Salary of employee :", "=", empData[k][2])

   """
