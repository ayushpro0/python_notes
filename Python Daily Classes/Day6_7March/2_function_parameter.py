# function defination

def display(x, y):      # x, y positional non-default args (mandatory)
    print("x = %d y = %d" %(x,y))


display(10, 20)

print("------------------------------------")

display(10, 20, "abc")
# TypeError: display() takes 2 positional arguments but 3 were given
print("END!!!")