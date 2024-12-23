dictionaryOne = {}
dictionaryTwo = {'course': 'moc', 'name': 'python', 'name': 'Perl'}

print("dictionaryTwo = ", dictionaryTwo)  # {'course': 'moc', 'name': 'Perl'}
print(dictionaryOne, dictionaryTwo)  # {} {'course': 'moc', 'name': 'Perl'}

print("name = ", dictionaryTwo['name'])  # Perl
print('name' in dictionaryTwo)  # True

if dictionaryTwo['name']:
    print("Name contains value")
else:
    print("No Value for name")

dictionaryTwo['course'] = 'Selfy'

# add new entry
dictionaryTwo['id'] = 100  # creates key-value pair 'id':100

print("dictionaryTwo = ", dictionaryTwo)  # {'course': 'Selfy', 'name': 'Perl', 'id': 100}

print("==========================================================")

# delete pair
del dictionaryTwo['id']
print("after deletion = ", dictionaryTwo)  # {'course': 'Selfy', 'name': 'Perl'}

dictionaryTwo.clear()
print("after clearing = ", dictionaryTwo)  # {}

dictionaryFour = {'name': 'python', 'course': 'moc'}
del dictionaryFour
# dictionaryFour   # => not accessible as deleted, NameError if try to access

dictionaryTwo = {'name': 'python', 'course': 'moc'}
print("Items = ", dictionaryTwo.items())  # dict_items([('name', 'python'), ('course', 'moc')])
print("dictionaryTwo.keys() = ", dictionaryTwo.keys())  # dict_keys(['name', 'course'])
print("dictionaryTwo.values() =", dictionaryTwo.values())  # dict_values(['python', 'moc'])

print("-----------------------------------------")

k1 = list(dictionaryTwo.keys())  # dict_keys(['name', 'course'])
k1.sort()

for i in k1:  # generic loop to process dictionary   ['course', 'name']
    print(i, "\t = ", dictionaryTwo[i])
    dictionaryTwo[i] = dictionaryTwo[i].upper()

print("-----------------------------------------")

print("Updated dictionaryTwo = ", dictionaryTwo)  # {'name': 'PYTHON', 'course': 'MOC'}

print("-----------------------------------------")

empData = {'3a': 50000, '1a': 30000, '2a': 40000}
print("Original Emp Data = ", empData)  # {'3a': 50000, '1a': 30000, '2a': 40000}

# Task: increment the salary of every person by 5000 and then display updated emp data
k1 = list(empData.keys())
print("K1 = ", k1)  # ['3a', '1a', '2a']

k1.sort()
print("Sorted K1 = ", k1)  # ['1a', '2a', '3a']

totalSal = 0
for i in k1:
    print("Emp Id : ", i, "\t Salary = ", empData[i])
    totalSal += empData[i]
    empData[i] += 10000

print("Updated Emp Data = ", empData)  # {'3a': 60000, '1a': 40000, '2a': 50000}
print("Total Sal = ", totalSal)  # 120000

print("-----------------------------------------")

# '5a':75000 add this pair in empData
empData['6a'] = 66000

empData.update({'5a': 75000})

str1 = input("Enter emp ID: salary in a single line: ")  # "7a :77000"
l1 = str1.split(":")  # l1 is a list of [id,sal]
print("list1 = ", l1)  # ['71', '77000']

empData[l1[0]] = l1[1]
print("Updated Emp Data = ", empData)
# {'3a': 60000, '1a': 40000, '2a': 50000, '6a': 66000, '5a': 75000, '71': '77000'}

print("-----------------------------------------")

empData1 = {'3a': ['ABC', 50000, 25], '1a': ['NIL', 65000, 30], '2a': ['XYZ', 85000, 45]}
print("Emp Data =", empData1)  # {'3a': ['ABC', 50000, 25], '1a': ['NIL', 65000, 30], '2a': ['XYZ', 85000, 45]}

print("Emp 1a details are =", empData1['1a'])  # list #['NIL',65000,30]
print("Emp 1a salary =", empData1['1a'][1])  # 65000

empData1['1a'][-1]  # age

empData2 = {
            '3a': {'Name': 'ABC', 'Sal': 50000, 'Age': 25},
            '1a': {'Name': 'NIl', 'Sal': 65000, 'Age': 30},
            }

print("Age of 3a emp = ", empData2['3a']['Age'])  # 25

"""
#assignment
emp ={'3a':50000,'1a':30000,'2a':40000}  
#1a 2a 3a are employee ID's    and 50000 30000  40000 are the values
e1=emp.keys()
e1.sort()
print "Sorted emp keys = ",e1
#add 1 emp details 4a:90000 , take this entry from user in 1 line
#increment the salary of every person by 5000
#finally display all emp details by sorting the id's

#emp.update({'4a':90000})
#keyboard inpu
empinput = rawinput("Enter name space sal")
empDatalist = empinput.split(" ")

"""

""""
emp ={'1a':30000,'2a':40000}
print "-----------------------------------------"
print "emp data"
for i in emp.keys():   #generic loop to process dictionary
    print i ,"\t = ",emp[i]
    emp[i]+=5000
print "-----------------------------------------"
print "Updated data"
for i in emp.keys():   #generic loop to process dictionary
    print i ,"\t = ",emp[i]
print "-----------------------------------------"

dictionary1 = {'id':100}
dictionary2 = {'name': 'python', 'course': 'moc'}
t1 = dictionary1, dictionary2
print "Tuple = ", t1
print t1[0].keys()
for d in t1:
    for i in d.keys():
        print "Key = ",i , "Value = ",d[i]
"""

"""
Assignment
Dictionary for employee data
key = emp id
value =salary
-display this data using for loop
-incraese the sal of every person by 10000
-display this updated data using for loop

emp[i] +=10000
"""
