import pandas as pd

arr = [31, 28, 31, 30]
month = ['jan', 'feb', 'march', 'april']

obj1 = pd.Series(data=arr, index=month)

print("obj1 = \n", obj1)
print("obj1.index = ", obj1.index)  # obj1.index =  Index(['jan', 'feb', 'march', 'april'], dtype='object')
print("obj1.values = ", obj1.values)  # obj1.values =  [31 28 31 30]
print("obj1.dtype = ", obj1.dtype)  # obj1.dtype =  int64

print("------------------------------------------")

obj2 = pd.Series([2.3, 5.5, 6.2])

print("obj2 = \n", obj2)
print("obj2.dtype = ", obj2.dtype)
print("obj2.item = ", obj2.item)

print("------------------------------------------")

import numpy as np

obj3 = pd.Series([2.3, np.NaN, 6.12, 4])

print("obj3 = ", obj3)
print("obj2.shape = ", obj2.shape, "obj3.shape = ", obj3.shape)
print("obj2.nbytes = ", obj2.nbytes, "obj3.nbytes = ", obj3.nbytes)
print("obj3.empty = ", obj3.empty)

print("------------------------------------------")

# Series Indexing Slicing
import pandas as pd

obj4 = pd.Series([5, 12, 23, 50])
print("obj4 = \n", obj4)

# how to access handle individual elements
print("obj4[2] = ", obj4[2])
# print("obj4[5] = ", obj4[5])  # KeyError : 5

# Extracting Slicing Series object
print("obj4[0:1] = \n", obj4[0:1])

print("obj4[1:3] = \n", obj4[1:3])

print("obj4[1:] = \n", obj4[1:])

print("------------------------------------------")

# modifying elements of series object value
obj4[0] = 15
print("obj4[0] = ", obj4[0])

obj4[1:4] = 22, 23, 24
print("obj4[1] = ", obj4[1])
print("obj4[2] = ", obj4[2])
print("obj4[3] = ", obj4[3])

print("obj4=\n", obj4)

print("------------------------------------------")

# Renaming Indexes
obj4.index = ['a', 'b', 'c', 'd']
print("obj4.index = ", obj4.index)
print("obj4=\n", obj4)

print("------------------------------------------")

# number of dimension
print("obj4.ndim = ", obj4.ndim)
print("obj4.nbytes = ", obj4.nbytes)

print("------------------------------------------")

# head() and tail() function
# head is used to fetch first n rows
print("obj4.head(2) = ", obj4.head(2))

# tail() is used to fetch the last n rows
print("obj4.tail(2) = ", obj4.tail(2))

print("------------------------------------------")

# vector operation on series object
# it means if you apply function or expression, then it applies to each element in the series

print("obj4+2 = ", obj4 + 2)

print("obj4*2 = ", obj4 * 2)

print("------------------------------------------")

# arithmatic on Series object
obj5 = pd.Series([2, 3, 4, 5])
print("obj5 = ", obj5)

obj6 = pd.Series([3, 6])
print("obj6 = ", obj6)

newobj = obj5 + obj6
print("newobj =\n", newobj)  # NaN--- Not a number

print("----------------------------------------------------")

# filtering entries
info = pd.Series(data=[31, 41, 51])
print("info = ", info)

print("output of info > 40 = \n", info > 40)

# condition fulfill only display that value & index
print(info[info > 40])

print("----------------------------------------------------")

# sorting Series object
a = pd.Series([10, 8, 15, 2])
print("a = ", a)

# a.sort_values()

print("a.sort_values() = \n", a.sort_values())

print("a.sort_values(ascending=False) = \n", a.sort_values(ascending=False))
