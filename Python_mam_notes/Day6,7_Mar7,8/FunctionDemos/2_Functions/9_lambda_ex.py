print(lambda: 1)
# this loads  a function without any name anonymous  ,
# after : is the return value  <function <lambda> at 0x00000000030829E8>

print("----------------------------------------------------")

x1 = lambda: 500
print("x1 ref = ", x1)  # <function <lambda> at 0x03874B30>
print("ret value of lambda fun referred by x1 = ", x1())

"""
while printing lambda expression as
lambda :1
it has its own string representation that python interpreter will follow as
<function <lambda> at 0x00000000033673C8>
"""

# call the lambda function
a = lambda: 100  # a is ref pointing to lambda function
print("a = ", a)  # <function <lambda> at 0x00000000030829E8>
print(a())  # control will be transferred to lambda annonymous function
print("--------------------------------------")


# 2nd example
def a1(num):
    print("In a1 function..................", num)


print(a1(10))
# interpreter will transfer the control to that anonymous function by passing 10 a1 parameter

# alternative
a1 = lambda x: x ** 2  # def func1(x):return x**2
result = a1(5)
print("Result = ", result)

# a1()  #TypeError: <lambda>() takes exactly 1 argument (0 given)

print("-----------------------------------------------------------------------------")

print((lambda: 5)())  # (lambda:5) this loads the anonymous function in memory
# ()   does the job of function call

print("-----------------------------------------------------------------------------")

#   functional programming in Python : map , filter, reduce   -----> lambda used very widely

d = lambda p: p * 2  # this is first lambda expression

r1 = d(5)
print("Result: ", r1)  # 10

r1 = d(15)
print("Result: ", r1)  # 30

print("***************************************")

print((lambda: 6)())  # this is a separate 2nd lambda expression   ans  = 6 and not 12

print((lambda s1: s1.upper())("hello"))

"""
#what's the difference between ->
print lambda:1      #this loads anonymous function in the memory (function is not invoked) O/p <function <lambda> at 0x00000000032113C8>
#and
print (lambda:1)()        #this loads anonymous function in the memory and calls it : o/p =1
"""
