# -*- coding: utf-8 -*-
"""
@author: Jamgaonkar
"""

# Write a pandas program to filter out rows based on different criteria such as duplicate rows. Program Description:
# This program selects duplicate rows from data frame on the basis of column name. Program Logic: Create dictionary
# say ‘Sales_data’ which contain detail information about product such as item category,item name,expenditure. Create
# DataFrame say ‘df’ using DataFrame method of pandas module and pass dictionary ‘Sales_data as an argument to
# DataFrame ‘df’ Use duplicated method of DataFrame to display all duplicate rows from DataFrame ‘df’ Apply
# duplicated method of DataFrame on column ‘Item_name‘ to display redundant rows on the basis of item name Apply
# duplicated method of DataFrame on column ‘Expenditure’ to display duplicate rows on the basis of expenditure.
# Display all result on console using print function Exit
import pandas as pd

Sales_data = {"Item_Category": ["Food", "Drink", "Food", "Sweet", "Food", "Sweet", "Drink", "Drink"],
              "Item_Name": ["Maggi", "Fruite", "PAsta", "Gulabjamun", "Maggi", "Ice-Cream", "Fruite", "Maza"],
              "Sales_Expenditure": [50, 20, 60, 100, 50, 65, 30, 40]}
df = pd.DataFrame(Sales_data)
print(df)
# display all duplicate rows from DataFrame ‘df’
print(df.duplicated(keep=False))
print(df[df.duplicated(keep=False)])
# display redundant rows on the basis of item name
print(df[df.duplicated("Item_Name", keep=False)])
# display duplicate rows on the basis of expenditure.
print(df[df.duplicated("Sales_Expenditure", keep=False)])
