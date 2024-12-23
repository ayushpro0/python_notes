# -*- coding: utf-8 -*-
"""
@author: Jamgaonkar
"""
# Write a program to import and export data between Pandas and CSV file with Practical Example.
# Write a program to Export data between dataframe and CSV with practical example
# Program Logic:
# Import pandas module in program using import statement
# Import numpy module using import statement
# Create Dictionary object say ‘marks’ with different set of key-value pair
# Create DataFrame object say ‘result’ using DataFrame method and pass index as argument to it
# Print DataFrame ‘result’ using print function
# Write dataframe object into csv file using to_csv method and pass data frame object as an argument to it

import pandas as pd
import numpy as np

marks = {"English": [67, 89, 90, 55],
         "Maths": [55, 67, 45, 56],
         "IP": [66, 78, 89, 90],
         "Chemistry": [45, 56, 67, 65],
         "Biology": [54, 65, 76, 87]}

result = pd.DataFrame(marks, index=["Athang", "Sujata", "Sushil", "Sumedh"])

print("******************Marksheet****************")
print(result)
print("-----------------------------------------------------------------")
print("Dataframe saved to CSV file successfully..")
result.to_csv("result1.csv")
