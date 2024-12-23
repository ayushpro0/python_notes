"""
Read file content of given file “empdata”, and print total sal.
File data:
1a:ABC:25:25000
2a:XYZ:30:30000
3a:LMN:45:60000
Hint: store the data in dictionary and then process

"""
f = open('empdata.txt')
empDict = {}

for line in f:
    x = line.split(":")  # x = ['1a', 'ABC', '25', '25000]
    empDict[x[0]] = x[1:]  # empDict['1a'] = ['ABC', '25', '25000]

print("empData = ", empDict)

total_sal = 0
for empid in empDict:
    total_sal += int(empDict[empid][-1])

print("total salary : ", total_sal)

""" # ---- Alternative Method -----


with open("empdata.txt", "r") as file:
    data = file.readlines()

emp_dict = {}

for line in data:
    emp_data = line.strip().split(":")
    emp_dict[emp_data[0]] = {"name": emp_data[1], "age": int(emp_data[2]), "salary": int(emp_data[3])}

total_sal = sum(emp_dict[emp]["salary"] for emp in emp_dict)

print(f"Total Salary: {total_sal}")
"""
