"""Variable number of args facility
*x variable is a speacila tuple variable capable of capturing only the excessing
positional/ non-keyword parameter passed
"""

def add(num1, num2, *x): # *x is special tuple variable
    print("x = ", x)
    return num1 + num2

print("Functions Learning...")

# add() # TypeError: add() missing 2 required positional arguments: 'num1' and 'num2'

add(num2 = 10, num1 = 20) # x = ()   | keyword args passing

# add(num2 = 9, 8) # SyntaxError: positional argument follows keyword argument

add(10, 20, 1, 2) # x = (1,2)

add(10, 20, [1,2,3,4]) # x =  ([1, 2, 3, 4],)

# add(1, 2, x1 = 100, y1 = 200) 
# TypeError: add() got an unexpected keyword argument 'x1'

print("END!!!")