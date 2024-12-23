# -*- coding: utf-8 -*-
"""
@author: Jamgaonkar
"""
# WAP pandas to create data frame quarterly sales where each row contain the item category, item name and expenditure
# Group the row by the category and print the total expenditure per category.
# Program Logic:

# Step1: Create Dictionary ‘Sales_data’

# Step2: Create Dataframe ‘Sales_quarterly’ using pd.DataFrame() method

# Step 3: Display DataFrame ‘Sales_quarterly’

# Step2: Use group by function on column ‘Item category’ to  calculate total expenditure  item_category ‘wise

# Step3: Apply aggregate function sum() to calculate the total expenditure ‘Item category’ wise.

# Step4: Display the resultant Dataframe

# ---------------------------------------------------------

import pandas as pd

Sales_data = {"Item_Category": ["Food", "Drink", "Food", "Sweet", "Food", "Sweet", "Drink", "Drink"],
              "Item_Name": ["Maggi", "Fruity", "Pasta", "Gulabjamun", "Momos", "Ice-Cream", "Pepsi", "Maza"],
              "Sales_Expenditure": [50, 20, 60, 100, 120, 65, 30, 40]}

Sales_quarterly = pd.DataFrame(Sales_data)

print("Dictionary Sales_data = ", Sales_data)

print("Dataframe Sales_quarterly :")
print(Sales_quarterly)

print("-------------------------------------------------------------------")

gdf = Sales_quarterly.groupby("Item_Category")
print("Group by item category :")
print(gdf)

Resulted_df = gdf["Sales_Expenditure"].sum()
print("Resulted_df :")
print(Resulted_df)
