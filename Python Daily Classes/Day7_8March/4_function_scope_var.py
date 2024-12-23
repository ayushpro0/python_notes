# Local and Global variables

def func1():
    global a
    # global b = 100 # SyntaxError: invalid syntax
    a = 1
    b = 2


# --------------------------------
# main module execution

print("Name of the current module = ", __name__)  # "__main__"

a = "One"
b = "Two"

func1()

print("a = ", a)  # a = 1 if a is global else a = "One"
print("b = ", b)  # b = "Two"
