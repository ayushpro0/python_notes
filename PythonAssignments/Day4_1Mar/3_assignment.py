# 3.	Accept the content from keyboard for empdata. Store it in a dictionary -“empdata”
# Print all emp details on separate lines.
# Print the total sal.

# Sample keyboard Input-
# 1a:25000
# 2a:30000
# 3a:60000

# Sample O/P
# Emp ID : 1a	Sal = 25000
# Emp ID :2a	Sal = 30000
# Emp ID :3a	Sal = 60000

# Total Salary = 115000

empData = {}

while True:
    input_str = input("Enter the ID and Salary Pair or q to quit : ")
    if input_str.lower() == 'q': break

    emp_id, salary = input_str.split(':')
    empData[emp_id] = int(salary)

print(empData)

total_salary = 0
for emp in empData:
    print("Emp ID :", emp, "\t", "Sal :", empData[emp])
    total_salary += empData[emp]

print("Total Salary : ", total_salary)
