#What will be the output of below code?

import re
print (re.sub("PSL","Persistent","Welcome to PSL, PSL in Pune")) #Welcome to Persistent, Persistent in Pune
print ("----------------------------------------------")


string = "If the the problem is textual, use the the re module"
print ("Original string = ",string) #Original string =  If the the problem is textual, use the the re module
pattern = r"the the"
regexp = re.compile(pattern)
str1=regexp.sub("the", string)
print ("Modified string = ",str1)    #Modified string =  If the problem is textual, use the re module












"""
Assignment
accept price field from a user(keyboard i/p)
Validate it for below rules-
1. it should begin with $
2. followed with at least 1 disgit
3. then decimal point .
4. then exact 2 number of digits after the decimal point


print the valid price field

price = "$1.55"       valid
price = "$.55"         Not valid
price = "$1.34555"      Not valid
"""










































       
