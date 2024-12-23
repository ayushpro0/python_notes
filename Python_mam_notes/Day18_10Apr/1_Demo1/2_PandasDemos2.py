# Practice Program
import pandas as pd

# data on python dictionary creating series(dictionary -- key value pair)
obj1 = pd.Series({'Jan': 31, 'feb': 28, 'march': 31})
print("obj1 = \n", obj1)

print("--------------------------------------------------------------------")

# W.A.Prog create series object using dictionary that store number of class 12
obj1 = pd.Series({'A': 31, 'B': 28, 'C': 31})
print("obj1 = \n", obj1)

print("--------------------------------------------------------------------")

# data as Scalar value
# data can be in the form of single value or a scalar value then index value of argument must be provided
obj1 = pd.Series(10, index=range(0, 1))
print("Obj1 = \n", obj1)

# obj1 = pd.Series(15,index=range(0,6,2))

obj1 = pd.Series(15, index=range(1, 6, 2))
print("Obj1 = \n", obj1)

print("--------------------------------------------------------------------")

obj1 = pd.Series("Yet to Start", index=['ND', 'Patna'])
print("Obj1 = \n", obj1)

print("--------------------------------------------------------------------")

# W.A.Prog Create Series object that store 50000 each quarter
obj1 = pd.Series(50000, index=['qtr1', 'qtr2', 'qtr3', 'qtr4', 'qtr5'])
print("obj1 = \n", obj1)


print("--------------------------------------------------------------------")

# Total no medals to be won is 200 in university game held alternate year to create series 2020--2029
obj1 = pd.Series(200, index=range(2020, 2029, 2))
print("obj1 = \n", obj1)

print("--------------------------------------------------------------------")
