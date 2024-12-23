# 3. Write a program to display the powers of 2 using anonymous function.

num = int(input("Enter the number : "))

print("Power of 2 of", num, " : ", (lambda x : x**2) (num))