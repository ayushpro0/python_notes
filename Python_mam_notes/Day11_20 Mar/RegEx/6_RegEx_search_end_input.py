import re

# s1 = raw_input("Enter single digit  :")  #in Python2.x
s1 = input("Enter single digit  :")  # in Python3.x

# m = re.search("^[0-9]$",s1) # to check if the given input is a single digit
m = re.search("^\d$", s1)  # same as above

if m is not None:
    print("Match found = ", m.group())  #
else:
    print("Match Not found!!!")
# match at the end only
