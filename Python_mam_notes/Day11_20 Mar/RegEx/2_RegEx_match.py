import re

s1 = "PSL Welcome to PSL. PSL, Pune"
s2 = "pslWelcome to PSL. PSL, Pune"  # match not found

pattern = r"PSL"  # raw string
m = re.match(pattern, s1)  # match at the beginning, sucessful
# m = re.match(pattern,s2)             #match at the beginning, not sucessful
print("m = ", m)  # match object

if m is not None:
    print("Match found content = ", m.group())  # match value is printed here
else:
    print("Match Not found!!!")

"""
#match at the begining only
path=R"c:\data\tew\new.txt"
print "Path =", path
print ""
"""
