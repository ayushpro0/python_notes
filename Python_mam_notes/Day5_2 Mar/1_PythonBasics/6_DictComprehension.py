"""
Dict Comprehnsion
"""
list1 = [1,2,3,4]
newDict ={i:i**2 for i in list1} #{1:1,2:4, 3:9, 4:16}
print("Original lsit1 = ", list1)
print("newDict = ", newDict)
print("---------------------------------------------------")

empData ={'1a':55000 , '2a':125000, '3a':45000, '4a' :145000}
print("Original empdata = ", empData)
newEmpData ={}#get the empData with sal>100000
newEmpData = { k:empData[k] for k in empData if empData[k]>100000}
print("newEmpData = ", newEmpData)#{'2a': 125000, '4a': 145000}
print("---------------------------------------------------")

