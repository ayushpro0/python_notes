'''3. Write a program to display the powers of2 using anonymous function.'''

n = int(input("Enter a number: "))
power = lambda x: x**2
print(power(n))