"""at import statement level
if __name__  == "__main__":
of module file will not be executed
"""

import mymath  # mymath.pyc

print("*********************************")

print("pi = ", mymath.pi)
print("area = ", mymath.area(5))
mymath.fib(35)
# print pi
print("Learning Modules")
print("End")
