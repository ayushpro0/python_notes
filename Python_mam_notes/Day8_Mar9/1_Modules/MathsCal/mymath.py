# module file defination  mymath.py
"""mymath - our example math module"""
pi = 3.14159


def area(r):
    """area(r): return the area of a circle with radius r."""
    return pi * r * r


# write Fibonacci series up to n
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a + b  # tuple


if __name__ == "__main__":  # this is True if this current module file is executed on its own
    print("=========================================================")
    fib(21)
    print("Area of circle with radius 5 = ", area(5))
    print("=========================================================")

#
"""
import sys
sys.path.append('D:/Python_Demos/Python Codes/Python Codes/4_Modules')
"""

"""
import sys
#fib(int(sys.argv[1]))
fib(21)

"""
