#1_Question:empData

n= int(input("Number of input:"))
empData = {}

for i in range(n):
    data = list(map(str, input('using : separator\n').split(':')))
    empData[data[0]] = data[1:]
    
tot_sal = 0
    
for i in empData:
    print('Emp ID:',i,' Details:')
    print('\tName:',empData[i][0])
    print('\tAge:', empData[i][1])
    print('\tSal:', empData[i][2])
    tot_sal+=int(empData[i][2])
    
print('Total Salary =', tot_sal)