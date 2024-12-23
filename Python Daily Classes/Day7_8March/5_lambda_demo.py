# lambda pre-defined keyword
def true():
    return 1


print("return value of true() : ", true())

print("----------------------------")

ref1 = lambda: 1  # function is loaded in the memory without any name
print("rf1 = ", ref1)  # rf1 =  <function <lambda> at 0x00000197F77098A0>

result = ref1()
print("result = ", result)  # result =  1

print("----------------------------")

print("Return value of lambda func call : ", (lambda: 55)())
# Return value of lambda func call :  55

print("----------------------------")

r1 = lambda x1: x1 ** 2
# r1()    # TypeError: <lambda>() missing 1 required positional argument: 'x1'

print("ret val of lambda : ", r1(5))
# ret val of lambda :  25

print("Upper Case = ", (lambda word: word.upper())("persistent"))
# Upper Case =  PERSISTENT

print("----------------------------")

print("Sum of 10 and 20 : ", (lambda num1, num2: num1 + num2)(10, 20))
# Sum of 10 and 20 :  30
