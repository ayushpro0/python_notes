import pandas as pd
import numpy as np

# array Slice
t1 = ((2, 4, 1, 6, 8), (3, 5, 6, 8, 9), (11, 12, 13, 14, 15), (21, 22, 23, 24, 25), (31, 35, 56, 22, 12))

n = np.array(t1)

print("numpy array n = \n", n)
print("n[:3,3:] = \n", n[:3, 3:])

print("----------------------------------------------------------------------")

# 1st row & till 2
# 1: = start of row1 till end
# ::2 = step to 2 rows
# :3 = col 0 to 2 don't include 3
print("n[0::2,:3] = \n", n[0::2, :3])

print("-----------------------------------Vstack-----------------------------------")

list1 = [1, 2, 3]
list2 = [4, 5, 6]
comb = np.vstack((list1, list2))
print("comb = \n", comb)
print("comb.shape = ", comb.shape)

print("----------------------------------Hstack------------------------------------")

comb = np.hstack((list1, list2))
print("comb = \n", comb)
print("comb.shape =  ", comb.shape)

print("----------------------------------------------------------------------")

# concatenate(combining of existing array)
array = (23, 32, 45)
array1 = (11, 54, 89)
array2 = (23, 43, 61)
concat = np.concatenate((array1, array2), axis=0)

print("array1 = ", array1)
print("array2 = ", array2)
print("concat of array1 and array2 = ", concat)

print("----------------------------------------------------------------------")

# slice your array
array = (23, 32, 45, 54, 76, 65, 9, 87)
print("array = ", array)

newarray = np.split(array, [2, 4, 6])
print("newarray = ", newarray)

print("----------------------------------------------------------------------")

array = ([[23, 32, 45, 54, 76, 65, 9, 87], [1, 2, 3, 4, 5, 6, 7, 8], [55, 44, 67, 54, 23, 34, 54, 87]])

newarray = np.split(array, [2, 8], axis=1)

print("array = ", array)
print("newarray = ", newarray)

print("----------------------------------------------------------------------")

# Dataframe Datastructure
# dataframes data in 2dimensional way
# how to create dataframe
# create dataframe object using 2D array
import pandas as pd

dict1 = {'student': ['amit', 'Nitu', 'Ramesh'],
         'marks': [80, 90, 60], 'sports': ['Cricket', 'Football', 'Hockey']}
df = pd.DataFrame(dict1, index=['a', 'b', 'c'])
print("Dictionary dict1 = ", dict1)
print("Dataframe df = \n", df)
print("----------------------------------------------------------------------")
# Given dictionary(value in list format)name that store section name in list format as values of section keys
# & contribution among list as values for country keys

# dict1={'section':['a','b','c','d'],'vontribution':[55000,65000,45000,30000]}
import pandas as pd

dict1 = {'section': ['a', 'b', 'c', 'd'], 'vontribution': [55000, 65000, 45000, 30000]}
df = pd.DataFrame(dict1)
print("Dictionary dict1 = ", dict1)
print("Dataframe df = \n", df)
print("----------------------------------------------------------------------")
# creating dataframe from 2D having values of dictionary object
import pandas as pd

dict1 = {'sales': {'Name': 'Rahul', 'Age': 23, 'Sex': 'Male'},
         'MKT': {'Name': 'Sham', 'Age': 33, 'Sex': 'Male'}}
df = pd.DataFrame(dict1)
print("Dictionary dict1 = ", dict1)
print("Dataframe df = \n", df)
print("----------------------------------------------------------------------")

# [list of dictionary]use in dataframe first u make lots of dictionary then all dictionary in list format
import pandas as pd

dict1 = {'RollNo': 101, 'Name': 'Ram', 'Marks': 78}
dict2 = {'RollNo': 102, 'Name': 'ABCD', 'Marks': 87}
dict3 = {'RollNo': 103, 'Name': 'XYZ', 'Marks': 178}
list1 = [dict1, dict2, dict3]
df = pd.DataFrame(list1)
print("Dictionary dict1 = ", dict1)
print("Dictionary dict2 = ", dict2)
print("Dictionary dict3 = ", dict3)
print("List1 = ", list1)
print("Dataframe df = \n", df)
print("----------------------------------------------------------------------")
# if u want to give index
df1 = pd.DataFrame(list1, index=['Sec1', 'Sec2', 'Sec3'])
print("Dataframe df = \n", df)
print("----------------------------------------------------------------------")
# Passing 2D List
import pandas as pd

list1 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
print("List1 = ", list1)
df = pd.DataFrame(list1)
print("Dataframe df = \n", df)
print("----------------------------------------------------------------------")
# row index
df1 = pd.DataFrame(list1, index=['row1', 'row2', 'row3'])
print("Dataframe df1 = \n", df1)
print("----------------------------------------------------------------------")
# Coumn & row index
df2 = pd.DataFrame(list1, index=['row1', 'row2', 'row3'], columns=['col1', 'col2', 'col3'])
print("Dataframe df2 = \n", df2)
print("----------------------------------------------------------------------")
# Creating Dataframe object from 2d Array
import pandas as pd
import numpy as np

array1 = np.array([[100, 202, 307], [400, 450, 500]])
print("List array1 = \n", array1)
df = pd.DataFrame(array1)
print("Dataframe df = \n", df)
print("----------------------------------------------------------------------")
df1 = pd.DataFrame(array1, columns=['one', 'two', 'three'], index=['First', 'Second'])
print("Dataframe df1 = \n", df1)
print("----------------------------------------------------------------------")

# creating Dataframe object from 2D Dictionary with values as series object
import pandas as pd

staff = pd.Series([10, 20, 30])
salary = pd.Series([10000, 20000, 30000])
school = {'people': staff, 'amount': salary}
df = pd.DataFrame(school)
print("Staff pd series = \n", staff)
print("salary pd series = \n", salary)
print("school dictionary  = \n", school)
print("Dataframe df = \n", df)
print("----------------------------------------------------------------------")

# creating Dataframe object from another Dataframe object
import pandas as pd

df = pd.DataFrame([10, 20, 30], [40, 50, 60])
print("Dataframe df = \n", df)
print("----------------------------------------------------------------------")
df1 = pd.DataFrame(df)
print("Dataframe df1 = \n", df1)
print("----------------------------------------------------------------------")
