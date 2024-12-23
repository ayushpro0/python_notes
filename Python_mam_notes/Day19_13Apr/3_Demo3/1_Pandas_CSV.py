# -*- coding: utf-8 -*-
"""
@author:Jamgaonkar
"""

# Importing and exporting data between pandas and CSV file.
# To create and open a data frame using ‘Student_result.csv’ file using Pandas.
# To display row labels, column labels data types of each  column and the dimensions
# To display the shape (number of rows and columns) of the CSV file.

import pandas as pd
import numpy as np
marks  = { "English" :[67,89,90,55],
           "Maths":[55,67,45,56],
            "IP":[66,78,89,90],
           "Chemistry" :[45,56,67,65],
           "Biology":[54,65,76,87]}
result = pd.DataFrame(marks,index=["Athang","Sujata","Sushil","Sumedh"])
print("******************Marksheet****************")
print(result)
result.to_csv("result.csv")
import csv

#Reading the Data
df = pd.read_csv("result.csv")
# Display Name of Columns
print("Columns: ",df.columns)

# Display no of rows and column
print("df shape = ",df.shape)

# For the Data frames created above, analyze, and plot appropriate charts with title and legend.
# • Show the Average score of each subject

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

df = pd.read_csv("result.csv")

# Show the Average score of each subject
y = ['English','Maths','IP','Chemistry','Biology']
width = [df['English'].mean(),df['Maths'].mean(),df['IP'].mean(),df['Chemistry'].mean(),
df['Biology'].mean()]

plt.figure(figsize = (12,2))
plt.barh(y = y, width = width)
plt.title('Average Scores')
plt.xlabel('Average Score')
plt.ylabel('Subjects')
for i,v in enumerate(width):
    plt.text(v, i, " "+str(round(v,2)), color='blue', va='center', fontweight='bold')
plt.show()
