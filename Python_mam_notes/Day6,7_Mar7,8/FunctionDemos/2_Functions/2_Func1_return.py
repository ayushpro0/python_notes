# Function Return value
def func2():
    print("In Func2....")


def func1():
    print("In func1.....")
    func2()

    # return "SUCCESS"  #return string
    return 'xyz', 1, 3.145  # return tuple


result = func1()  # calling function
print("Result return value = ", result)
