
import re
#s1 = raw_input("Enter sigle digit  :")  #in Python2.x
s1 = input("Enter sigle digit  :")  #in Python3.x
#m = re.search("^[0-9]$",s1)
m = re.search("^\d$",s1)

if m!=None:
    print ("Match found = ",m.group())   #
else:
    print ("Match Not found!!!")
#match at the end only

