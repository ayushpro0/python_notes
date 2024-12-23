# 1.	Accept the content from keyboard for empdata.
# Store it in a dictionary - “empdata”
# Print all emp details on separate lines.
# Print the total sal.

# 1a:ABC:25:25000
# 2a:XYZ:30:30000
# 3a:LMN:45:60000
# Hint: store the data in dictionary and
# then process, 1a, 2a, 3a are the keys and rest all is the value section data respectively.


# Sample O/P
# Emp ID : 1a	Details:
# 	Name: ABC
# 	Age : 25
# 	Sal : 25000
# Emp ID : 2a	Details:
# 	Name: XYZ
# 	Age : 30
# 	Sal : 30000
# Emp ID : 1a	Details:
# 	Name: LMN
# 	Age : 45
# 	Sal : 60000

# Total Salary = 115000


empData = {}

while True:
    input_str = input("Enter the employee details or q to quit : ")
    if input_str.lower() == 'q':
        break

    emp_id, name, age, sal = input_str.split(':')

    temp_dict = {}
    temp_dict["Name"] = name
    temp_dict["Age"] = int(age)
    temp_dict["Sal"] = int(sal)

    empData[emp_id] = temp_dict

totalSal = 0

for emp in empData:
    print("Emp ID :", emp, " Details :")
    print("\tName : ", empData[emp]["Name"])
    print("\tAge : ", empData[emp]["Age"])
    print("\tSal : ", empData[emp]["Sal"])
    totalSal += empData[emp]["Sal"]

print("Total Salary = ", totalSal)
