# at import statement level
# if __name__ == "__main__"
# of module file will not be executed

# import mymath #mymath.pyc  # do this if module is present in the same directory
# warna niche wale method se karna hoga

import sys
print("sys.path = ", sys.path)
sys.path.append(r"C:\Users\ayush\Documents\Persistent Training\python_tut\Python Daily Classes\Day8_9March\modules")

import mymath

print("***************************************")

print("pi = ", mymath.pi)

print("area = ", mymath.area(5))

mymath.fib(35)

# print(pi) #NameError: name 'pi' is not defined

print("Learning Modules")

print("END")