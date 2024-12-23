import re
regex = r"[a-zA-Z]+ \d+"
matches = re.findall(regex, "June 24, August 9, Dec 12")
print ("matches list = ", matches)
#matches is a  list
for match in matches:
    print ("Full match: %s" % (match)   )
"""
Full match: June 24
Full match: August 9
Full match: Dec 12
"""
print ("---------------------------------------------------------")
# To capture the specific months of each date we can use the following pattern
regex = r"([a-zA-Z]+)"
matches = re.findall(regex, "June 24, August 9, Dec 12")
for match in matches:
    print ("Match month: %s" % (match))
"""
Match month: June
Match month: August
Match month: Dec
"""
print ("---------------------------------------------------------")
# If we need the exact positions of each match
regex = r"([a-zA-Z]+) \d+"
matches = re.finditer(regex, "June 24, August 9, Dec 12")    #matches is a list of each match object
print ("matches object = ", matches)
for match in matches:
    print ("Match at index: %s, %s" % (match.start(), match.end()))















"""
Match at index: 0, 7
Match at index: 9, 17
Match at index: 19, 25
"""
