# 6.Write a program to display below Star (asterisk) patterns in Python.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

for i in range(0, 5):
    for j in range(0, i + 1):
        print("*", end=" ")
    print()
