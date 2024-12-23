import csv

filename = "employee_birthday.txt"

rows = []

# reading csv file
with open(filename, 'r') as csv_file:
    # creating a csv reader object
    csv_reader = csv.reader(csv_file)

    # extracting each data row one by one
    for row in csv_reader : 
        rows.append(row)
    
    # get total number of rows:
    print("total no. of rows :", csv_reader.line_num)   


# printing rows
print("\nrows data from a file: \n")
for row in rows:
    # parsing each column of a row
    for col in row:
        print(col, end="\t")
    print("\n")

print(rows)