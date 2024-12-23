"""
lambda pre - defined keyword
"""


def true():
    return 1


print("return val of true() func call = ", true())
print("----------------------------------------------------")

ref1 = lambda: 1  # function is loaded in the memory without any name
print("ref1 = ", ref1)  # =  <function <lambda> at 0x11047a8c0>
result = ref1()
print("result = ", result)
print("----------------------------------------------------")

print("Return value of lambda func call = ", (lambda: 55)())

print("----------------------------------------------------")

r1 = lambda x1: x1 ** 2
# r1()#TypeError: <lambda>() missing 1 required positional argument: 'x1'
print("ret val of lambda = ", r1(5))

print("----------------------------------------------------")

print("Upper case = ", (lambda word: word.upper())("persistent"))

print("----------------------------------------------------")

print("Addition = ", (lambda num1, num2: num1 + num2)(10, 20))
