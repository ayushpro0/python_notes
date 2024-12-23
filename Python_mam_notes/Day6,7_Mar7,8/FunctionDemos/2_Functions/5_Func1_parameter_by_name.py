# parameter by name: Keyword arguments

def greet(title, name):
    print("Hello " + title + " " + name)
    print("Lower case string = ", name.lower())


greet("Sangita", "Mrs.")  # # Hello Sangita Mrs.

print("--------------------------------------------------------------")

greet(name="ABC", title="Mr.")  # keyword arguments passing to a function call


print("--------------------------------------------------------------")

# greet(title="Mr.", "NIL")
# "NIL" as normal parameter (non-keyword argument)
# ---this can not be passed after keyword argument
# Syntax error

print("--------------------------------------------------------------")

# greet("NIL", title="Mr.") #TypeError: greet() got multiple values for argument 'title'

print("--------------------------------------------------------------")

# greet("Mr", name="NIL", value =100)#TypeError: greet() got an unexpected keyword argument 'value'
