# -*- coding: utf-8 -*-
"""
@author: Jamgaonkar
"""

import pandas as pd


def Ser_stumarks():  # Function definition
    print("In function : ")

    std_marks = []  # list

    for i in range(1, 6):
        m = int(input("Enter the Percentile:"))
        std_marks.append(m)

    s = pd.Series(index=range(1201, 1206), data=std_marks)
    print("Data fetched from the series are:")
    print("Entire Series Data :")
    print(s)

    print("-------------------------------------------------------")

    print("Series items with greater than 75 values: ")
    print(s[s >= 75])


Ser_stumarks()  # calling the above function
