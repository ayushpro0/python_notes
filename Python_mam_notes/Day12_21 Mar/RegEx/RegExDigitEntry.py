import re
"""
str1 =input("Enter 2 digit number only")

if re.search("^\d{2}$", str1)!= None:
    #num = int(str1)
    print("num =", str1 , "type = ", type(str1))
else :print("Invalid number entry... Try again!!!!!")
"""
s = "$12.55"
print('Yes' if re.search('^\$\d+\.\d{2}$' , s) else 'No')


^\$\d{1,}.\d{2}$ 
