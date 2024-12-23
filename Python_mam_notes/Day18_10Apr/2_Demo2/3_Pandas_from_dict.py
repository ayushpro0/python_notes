"""
@author:   JAMGAONKAR
"""

# Create a panda’s series from a dictionary of values and a ndarray

import pandas as pd
import numpy as np

s = pd.Series(np.array([1, 3, 4, 7, 8, 8, 9]))

print("Panda’s series  :")
print(s)

print("---------------------------------------------------------------------")

#  create a dictionary 
dictionary = {'X': 10, 'Y': 20, 'Z': 30}  # create a series
print("Dictionary = ", dictionary)

series = pd.Series(dictionary)

print("Panda’s series from a dictionary :")
print(series)
