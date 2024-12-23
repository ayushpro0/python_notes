

import re

s1="Welcome\n123 PSL. PSL, Pune. year2015ends"
s2="Welcome\nto PSL. PSL, Pune. year2015ends"

#m = re.search("([a-zA-Z]+)(\s+)([a-zA-Z]+)",s1)   #Match Not Found
m = re.search("([a-zA-Z]+)(\s+)([a-zA-Z]+)",s2)   # (Welcome) (\n) (to)

print ("m = ", m)
if m!=None:
    print ("Match Found = ",m.group())     #complete match
    print ("Match Found = ",m.group(0))   #complete match
    print ("Match Found = ",m.group(1))   #first()group match     o/p= Welcome
    print ("Match Found = ",m.group(2))   #second()group match    o/p=
    print ("Match Found = ",m.group(3))   #third()group match     o/p= to
else:
    print ("Match Not found!!!")


















#search anywhere first occurance only
"""
[a-z]+
[A-Z]
[0-9]   match any 1 gigit                                        \d    \d+
[^0-9]   negation    match for anythiong else other that a digit  \D
[ \t\n\r\f]  whitespaces                                          \s    \s+
[^ \t\n\r\f] non whitespaces                                      \S

[a-zA-Z0-9_]   alphanumeric word character                          \w
[^a-zA-Z0-9_]   non alphanumeric word character                     \W
"""
