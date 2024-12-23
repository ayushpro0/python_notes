"""
Variable number of args facility
*x variable is a special tuplem variable capable of capturing
onlt the excessive positional/ non-keyword parameter passed
"""


def add(num1, num2, *x):  # *x is special tuple variable
    print("x = ", x)  # x[0][0]
    return num1 + num2


print("Functions Learning....")

# add() #TypeError

add(10, 20, 1, 2)  # x = (1,2)

add(num2=9, num1=8)  # x = ()  keyword agrs passing

# add(num2 = 9,8)  # SyntaxError

add(10, 20, [1, 2, 3, 4])  # x = ([1,2,3,4])

add(1, 2, x1=100, y1=200)

print("END!!")

# pass a list as parameter, square all the elements inside the function
# and cross verify if the original list is modified...
