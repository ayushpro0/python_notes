
#creating a sub class
#Exception is pre defined class, create user defined class MYError as subclass of Exception
# in java ----> class AgeError extends Exception{}

class MyError(Exception):   #inheritance
    
    pass
#a = MyError()
#-------------------------------------------------------------

#raise MyError("Some information about what went wrong")


try:
   
    raise MyError("Some information about what went wrong")#constructor is called, object is created
    #and then it is raised to then except block

except MyError as a:
    print("Situation:", a)


print ("Prgrom proceeds.............")










"""
try:
    
    raise MyError("Some information about what went wrong")

except MyError as error:
    print("Situation:", error)
"""


"""

class Employee:       18    to 50  

    
class AgeError(Exception):
    pass

if (age<18 or age>50):
    raise AgeError("")
    
"""
