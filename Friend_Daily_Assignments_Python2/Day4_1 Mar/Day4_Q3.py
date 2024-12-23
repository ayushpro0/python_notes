'''3.	Accept the content from keyboard for empdata. Store it in a dictionary -“empdata”
Print all emp details on separate lines.
Print the total sal.

Sample keyboard Input-
1a:25000
2a:30000
3a:60000
'''

a = 'yes'
empdata = {}
while(a=='yes'):
    x = input("Enter details using : separator: ").split(':')
    #print("id: {}  salary: {}\n".format(x[0], x[1]))
    empdata[x[0]] = x[1]
    a = input("Want to put another details: yes/no \n")
sal = 0
for i in empdata:
    print("id: {}  salary: {}\n".format(i, empdata[i]))
    sal+=int(empdata[i])

print("Total Salary:  ", sal)



