'''Read file content of given file “empdata”, and print total sal.
File data:
1a:ABC:25:25000
2a:XYZ:30:30000
3a:LMN:45:60000
Hint: store the data in dictionary and then process
'''

file1 = open('empdata.txt','r')
cnt = file1.readlines()
#dic = {}
sal = 0

for i in cnt:
    i=i.split(":")
    #dic[i[0]] = i[-1]
    sal+=int(i[-1])

print("Total Salary: ",sal)


