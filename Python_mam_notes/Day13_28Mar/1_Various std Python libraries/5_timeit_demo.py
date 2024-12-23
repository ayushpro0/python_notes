from timeit import Timer
t1 = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
print ("t1 =", t1)
#0.57535828626024577
t2 = Timer('a,b = b,a', 'a=1; b=2').timeit()
print ("t2 =", t2 )
#0.54962537085770791

"""
Some Python users develop a deep interest in knowing the relative performance of different approaches
to the same problem. Python provides a measurement tool that answers those questions immediately.

For example, it may be tempting to use the tuple packing and unpacking feature instead of the traditional
approach to swapping arguments. The timeit module quickly demonstrates a modest performance advantage:
"""
"""
import math
math.sqrt(25)

from math import sqrt
sqrt(25)


from math import *
cos()
sqrt()
"""
