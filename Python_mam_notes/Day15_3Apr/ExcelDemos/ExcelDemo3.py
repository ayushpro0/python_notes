# import openpyxl module
import openpyxl

# Call a Workbook() function of openpyxl
# to create a new blank Workbook object
wb = openpyxl.Workbook()

# Get workbook active sheet
# from the active attribute.
sheet = wb.active

# writing to the cell of an excel sheet
sheet['A1'] = 2
sheet['A2'] = 3
sheet['A3'] = 4
sheet['A4'] = 5
sheet['A5'] = 6

# The value in cell A7 is set to a formula
# that sums the values in A1, A2, A3, A4, A5 .
sheet['A7'] = '= SUM(A1:A5)'


# The value in cell A7 is set to a formula
# that multiplies the values in A1, A2, A3, A4, A5 .
sheet['A8'] = '= PRODUCT(A1:A5)'


# The value in cell A7 is set to a formula
# that return average of the values in A1, A2, A3, A4, A5 .
sheet['A9'] = '= AVERAGE(A1:A5)'
# save the file
wb.save("sum.xlsx")


