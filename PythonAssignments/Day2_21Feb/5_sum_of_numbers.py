# 5.Calculate the sum of all numbers from 1 to a given number

num = int(input("Enter the number \n"))
result = 0
for i in range(1, num+1):
    result = result + i

print("The sum of all numbers between 1 and", num, "is =", result)