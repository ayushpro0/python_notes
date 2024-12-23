# functions
def func1():  # function definitions
    print("In func1.....")
    func2()  # return value is None


def func2():
    print("In Func2....")  # return value is None


# main script
print("Learning Functions...............")
print(func1())  # invoking/calling a function
print("---------------------------------------------")
print(func2())  # printing the return value
print("---------------------------------------------")
func3()  # NameError: name 'func3' is not defined
print("END!!!!")

"""
a=100
b=10
print "A ID = ", id(a)
print "B ID = ", id(b)

if a is b:
    print "TRUE"
else:
    print "FALSE"
print "-------------------------------------"
b=100
print "A ID = ", id(a)
print "B ID = ", id(b)
if a is b:
    print "TRUE"
else:
    print "FALSE"



"""

"""
def func2():                     #function definations
    print "In Func2...."

    def func3():
        print "In Func3...."

    def func1():
        print "In func1....."

        func2()

        return "Hello"
"""
