

"""
Complex data structures
1. Dict with list as value
1. Dict with dict as value
"""

empData = {'1a':{"Name":"ABC", "Age":24, "Sal":25000},
            '2a':{"Name":"xyz", "Age":35, "Sal":95000},
           }
print("empData = ", empData, "type = ", type(empData))
print("Details of 1a = ", empData['1a'], type(empData['1a']))#{"Name":"ABC", "Age":24, "Sal":25000}
print("Name of empID 1a = ", empData['1a']["Name"])

for k in empData:
    print("Details of empid ", k, " = ", empData[k])
print("---------------------------------------------------------")
#nested loop to traverse over the inner list 1 by 1:

for k in empData:
    print("Details of empid ", k, " : ")
    for k1 in empData[k]:
        print("\t", k1, " = ", empData[k][k1])  # inner dict's key
        if k1 == "Sal":
            empData[k][k1] += 10000

print("---------------------------------------------------------")

# increase the sal of every emp by 10000
print("empData = ", empData, "type = ", type(empData))


