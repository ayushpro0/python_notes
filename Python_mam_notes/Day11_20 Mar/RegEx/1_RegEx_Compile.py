import re

print("------------------------------------------------------")

regexp = re.compile("PSL")
# "PSL"  as pattern to be searched where in a given original string

s1 = "PSLaaaaa Welcome to aaaaaa. PSL persistent......"  # match found
s2 = "aaaaa PSL Welcome to aaaaaa. persistent......"  # match not found  as function returns  None

if regexp.match(s1):  # match function matches the pattern at beginning only
    print("Match found : ")

else:
    print("Match Not found")
print("------------------------------------------------------")

"""
The re module provides regular expression tools for advanced string processing.
For complex matching and manipulation, regular expressions offer
optimized string solutions:


"""
