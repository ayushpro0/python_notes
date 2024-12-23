# -*- coding: utf-8 -*-
"""
@author:  Jamgaonkar
"""
# Write a pandas program to create data frame for examination result and display row labels,
# column labels data types of each column and the dimensions with Practical Example.
# Program Logic:

# 1.Create Dictionary say ‘marks’ which contain marks of 5 subject namely English,Maths,IP,Chemistry,Biology and
# total marks obtained and percentage of students

# 2.Create DataFrame say ‘result’ using DataFrame method of pandas library

# 3.Print the mark sheet of 4 student

# 4.Use index attribute of DataFrame method to display row labels of dataframe named ‘result’

# 5.Use columns attribute of DataFrame method to display column labels of dataframe named ‘result’

# 6.Use dtypes attribute of DataFrame method to display data types of each column

# 7.Use ndim attribute of DataFrame method to display dimension of dataframe named ‘result’

# 8.Use shape attribute of DataFrame method to display shape of dataframe named ‘result’

# 9.Exit

import pandas as pd

Exam_data = {"English": [40, 50, 60, 70, 80],
             "Maths": [56, 43, 55, 68, 89],
             "Science": [66, 88, 90, 67, 76],
             "Marathi": [56, 89, 67, 55, 76]}

print("Exam_data : ")
print(Exam_data)

# Total = print(Exam_data['English'][0]+Exam_data['Maths'][0]+Exam_data['Science'][0]+Exam_data['Marathi'][0],Exam_data['English'][1]+Exam_data['Maths'][1]+Exam_data['Science'][1]+Exam_data['Marathi'][1],Exam_data['English'][2]+Exam_data['Maths'][2]+Exam_data['Science'][2]+Exam_data['Marathi'][2],Exam_data['English'][3]+Exam_data['Maths'][3]+Exam_data['Science'][3]+Exam_data['Marathi'][3],Exam_data['English'][4]+Exam_data['Maths'][4]+Exam_data['Science'][4]+Exam_data['Marathi'][4])

Result = pd.DataFrame(Exam_data, index=("Rahul", "Rohit", "Suman", "Aman", "Sagar"))

print("Result Dataframe : ")
print(Result)

print("Row Label Result.index = \n", Result.index)  # Row Label
print("Column Label Result.columns = \n", Result.columns)  # Column Label
print("datatype : ")
print(Result.dtypes)  # datatype
print("dimensions ndim : ", Result.ndim)
print("Shape : ", Result.shape)



# ----------------------------------------------------------------------------------
# import pandas as pd
#
# # 1. Create a dictionary with student marks
# marks = {
#     'English': [80, 75, 85, 90],
#     'Maths': [90, 85, 95, 80],
#     'IP': [70, 75, 80, 85],
#     'Chemistry': [85, 90, 80, 75],
#     'Biology': [95, 85, 90, 80],
#     'Total Marks': [420, 410, 430, 410],
#     'Percentage': [84, 82, 86, 82]
# }
#
# # 2. Create the DataFrame
# result = pd.DataFrame(marks, index=("Rahul", "Rohit", "Suman", "Aman"))
#
# # 3. Print the mark sheet of 4 students
# print(result)
#
# print("----------------------------------------------------------")
#
# # 4. Display row labels
# print("Row Labels:", result.index)
#
# # 5. Display column labels
# print("Column Labels:", result.columns)
#
#
# # 6. Display data types of each column
# print("Data Types:")
# print(result.dtypes)
#
# # 7. Display dimension of the DataFrame
# print("Dimension:", result.ndim)
#
#
# # 8. Display shape of the DataFrame
# print("Shape:", result.shape)
#
# # 9. Exit
