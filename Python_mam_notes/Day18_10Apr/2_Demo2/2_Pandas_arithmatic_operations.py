# -*- coding: utf-8 -*-
"""
@author:  JAMGAONKAR
"""

# Write a Pandas program to perform arithmetic operations on two Pandas Series.
import pandas as pd

ds1 = pd.Series([3, 6, 9, 12, 15])
ds2 = pd.Series([2, 4, 6, 8, 10])


print("Add two Series:")
ds = ds1 + ds2
print(ds)

print("Subtract two Series:")
ds = ds1 - ds2
print(ds)

print("Multiply two Series:")
ds = ds1 * ds2
print(ds)

print("Divide Series1 by Series2:")
ds = ds1 / ds2
print(ds)
