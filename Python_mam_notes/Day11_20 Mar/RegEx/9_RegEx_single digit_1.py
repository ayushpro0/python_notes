
import re
s= "Welcome to PSL. PSL, Pune. year2019ends"

m = re.search("\d+", s)  # match multiple  digits
print("m = ", m)
if m != None:
    print("Match Found = ", m.group())
else:
    print("Match Not found!!!")

# search anywhere first occurance only
"""
[a-z]+
[A-Z]
[0-9]   match any 1 gigit                                        \d    \d+
[^0-9]   negation    match for anythiong else other that a digit
[ \t\n\r\f]  whitespaces
"""
