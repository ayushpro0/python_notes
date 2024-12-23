# importing csv module
import csv

# csv field names
fields = ['Name', 'Branch', 'Year', 'CGPA']

# data rows of csv file
rows = [ ['Nikhil', 'COE', '2', '9.0'], 
		['Sanchit', 'COE', '2', '9.1'], 
		['Aditya', 'IT', '2', '9.3'], 
		['Sagar', 'SE', '1', '9.5'], 
		['Prateek', 'MCE', '3', '7.8'], 
		['Sahil', 'EP', '2', '9.1']] 

# name of csv file
filename = "university_records11.csv"

# writting to csv file
with open(filename, 'w') as csv_file:
    #creating a csv writer object
    csv_writer = csv.writer(csv_file)

    # writing the fields
    csv_writer.writerow(fields)

    # writing the data rows
    csv_writer.writerows(rows)
    