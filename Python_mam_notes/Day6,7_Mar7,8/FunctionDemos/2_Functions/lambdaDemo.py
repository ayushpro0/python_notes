"""
lambda- anonymous function
"""


def true():
    return 1


ref1 = lambda: 1  # memory is allocated like a function memory
print("ref1 = ", ref1)  # <function <lambda> at 0x107eb2830>
print("return val of lambda call = ", ref1())  # 1

print("lambda o/p = ", (lambda: 50)())  # 50

# print((lambda x : x**2)())
# TypeError: <lambda>() missing 1 required positional argument: 'x'

print((lambda x: x ** 2)(5))  # 25
print((lambda word: word.upper())("ayush"))  # AYUSH
