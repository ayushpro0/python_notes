'''Write a program to display below Star (asterisk) patterns in Python.
* 
* * 
* * * 
* * * * 
* * * * * 
'''

n = int(input("Enter range: "))
for i in range(1, n+1):
    for j in range(1,i+1):
        print("*",end = ' ')
    print()
