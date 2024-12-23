#function definition
#def display(x,y=1):#x positional non-default args (mandatory), y default

def display(x=1, y):
    print("x = %d y = %d "%(x,y))


def display1():                          #Function Def
    print("Inside display1 function....")

print("Learning Functions in Python!!!!")
display(10,20)                               #Calling a Function


display(199)  # x = 199 y = 1

print("END!!")

