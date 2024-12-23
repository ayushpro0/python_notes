print("Learning Exception Handling...")

# print(a) # NameError termination

"""
Python Interpreter raises an object of pre-defined Exception Class
NameError, Object is given to the console, object error description is printed on the console and then terminates the program.


ob1 = NameError() # creating an object of class nameError

so now, instead of termination of the program, lets capture the error within the code
Exception Handling : try except finally raise
try:
    pass
except(Nameerror as n1) :
    pass # to catch the error and handle it / corrective action
"""

try:
    print("Inside try section...")
    print(a1)

except NameError as n1:
    print("Error = ", n1)

print("END!!!")