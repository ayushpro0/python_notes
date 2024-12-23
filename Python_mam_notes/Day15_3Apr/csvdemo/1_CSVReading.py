# importing csv module 
import csv 

# csv file name 
filename = "employee_birthday.txt"

# initializing the rows list 
rows = [] 

# reading csv file 
with open(filename, 'r') as csvfile: 
	# creating a csv reader object 
	csvreader = csv.reader(csvfile) 
	
	# extracting each data row one by one 
	for row in csvreader: 
		rows.append(row) 

	# get total number of rows 
	print("Total no. of rows: %d"%(csvreader.line_num)) 

# printing rows 
print('\nrows data from a file:\n') 
for row in rows: 
	# parsing each column of a row 
	for col in row: 
		print("%10s"%col), 
	print('\n') 
