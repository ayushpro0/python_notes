""" 
@author:   JAMGAONKAR
"""
# Write a Pandas program to add some data to an existing Series.

import pandas as pd

s = pd.Series(['S101', 'Amjad', 'C.Sc.', 'XII – A1', '450'])

print("Original Data Series:")
print(s)

print("\nData Series after adding some data:")
new_s = s.append(pd.Series(['90.0', 'PASS']))
print(new_s)
