# dataframe object or u can say Function
import pandas as pd

dict1 = {'sales': {'Name': 'Rahul', 'Age': 23, 'Sex': 'Male'},
         'MKT': {'Name': 'Sham', 'Age': 33, 'Sex': 'Male'}}

df = pd.DataFrame(dict1)

print("dict1 = ", dict1)
print("Dataframe df = \n", df)

print("----------------------------------------------------------------------")

print("df.index = ", df.index)
print("df.columns = ", df.columns)
print("df.axes = ", df.axes)

print("----------------------------------------------------------------------")

print("df.dtypes = \n", df.dtypes)

print("----------------------------------------------------------------------")

print("----------------------------------------------------------------------")

# number of axes & dimensions
print("df.size = ", df.size)
print("df.shape = ", df.shape)
print("df.ndim = ", df.ndim)

print("df.empty = ", df.empty)
print("len(df) = ", len(df))

print("----------------------------------------------------------------------")

print("df.count()= \n", df.count())

print("df.count(0)= \n", df.count(0))
print("df.count(1)= \n", df.count(1))


print("df.count(axis='index')= \n", df.count(axis='index'))
print("df.count(axis='columns')= \n", df.count(axis='columns'))

print("----------------------------------------------------------------------")

# Transposition dataframe rows=columns & columns=rows
print("df.T = \n", df.T)

print("----------------------------------------------------------------------")

print("df.values = \n", df.values)

print("----------------------------------------------------------------------")
