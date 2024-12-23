'''1.	Accept 2 numbers from user and print addition, subtraction.'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition of two number: ", num1+num2)
if num1>num2:
    print("Subtraction of two number: ", num1-num2)
else:
    print("Subtraction of two number: ", num2-num1)