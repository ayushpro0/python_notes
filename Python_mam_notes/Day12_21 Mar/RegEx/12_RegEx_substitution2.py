
import re

# Lets try and reverse the order of the day and month in a date 
# string. Notice how the replacement string also contains metacharacters
# (the back references to the captured groups) so we use a raw 
# string for that as well.
regex = r"([a-zA-Z]+) (\d+)"
#(\1)(\2)
# This will reorder the string and print:
#   24 of June, 9 of August, 12 of Dec
replacement = r"\2 \1"
s1 = "June 24, August 9, Dec 12"
print (re.sub(regex, replacement, s1)) #24 June, 9 August, 12 Dec
#-----------------------------------------------------------------------------------------
"""
htmltag = "<img>Image Text</img>
#or
#htmltag = "<a>Anchor tag</a>

validate a given html tag for img or a tag

pattern =r"^<(img)>[\w\s]+<\/\1>$"   

replacement = r"\2  \1"
"""













       
