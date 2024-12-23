

def display(x, y = 1):      # x -> positional non-default args(mandatory), y default
    print("x = %d y = %d" %(x,y))

# def display(x = 1, y): # SyntaxError: Non-default argument follows default argument
#     print("x = %d y = %d" %(x,y))

display(10, 20) # x = 10 y = 20

display(199) # x = 199 y = 1
print("END!!!")