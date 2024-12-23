# function definition

def display(x, y):  # x, y positional non-default args (mandatory)
    print("x = %d y = %d  " % (x, y))


def display1():  # Function Def
    print("Inside display1 function....")


print("Learning Functions in Python!!!!")

display(10, 20)  # Calling a Function


# display(10, 20, "abc")  # TypeError: display() takes 2 positional arguments but 3 were given
print("END!!")
