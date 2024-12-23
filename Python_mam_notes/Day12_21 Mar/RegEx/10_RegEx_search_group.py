
import re

regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex, "June 24")

print ("Match at index %s, %s" % (match.start(), match.end()))
print ("Full match: %s" % (match.group(0)))    #match.group()   complete match    June 24
print ("Month: %s" % (match.group(1)) )   #June
print ("Day: %s" % (match.group(2))   )   #24
print ("------------------------------------------------------------------------------")
print (dir(re))     #list of all functionalities available in re module
print ("------------------------------------------------------------------------------")


# If we want, we can use the MatchObject's start() and end() methods 
# to retrieve where the pattern matches in the input string, and the 
# group() method to get all the matches and captured groups.















"""
"PSL|PUne|IBM"
"a|b|c|d"      [abcd]   charcter class group
[a-z]   [^a-z , A-Z]  negation
[0-9]                                           \d   digit match
[^0-9]                                          \D    non digit match
[a-zA-Z0-9_] alphanumeric word charcter         \w
[^a-zA-Z0-9_] NON alphanumeric word charcter    \W
[ \t\n\r\f]  white space charcter               \s
[^ \t\n\r\f]  white space charcter               \S


s= "fgdfgdgfgh9a"
re.match("^\d$", s)   "1"   "1gffgffgffgffgd5"


\D$
"""















