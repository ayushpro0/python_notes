import re

s = "\nPune PSL Welcome to PSL. PSL, Pune."  # Match found
s1 = "\n Pune PSL Welcome to PSL. PSL, Pune*"  # Match Not found

# m = re.search("Pune\.$",s)    # Match found =  Pune.
m = re.search(".", s)  # . metacharacter matches to any 1 single chr except \n => Match found =  P

if m != None:
    print("Match found = ", m.group())  # Pune
else:
    print("Match Not found!!!")
# match at the end only

"""
. + ? * | [ ] { } () ^  $  \   special Meta characters
$ if for end search
"pattern$"
. meta character searches for any one character   except \n






"."  dot charcheter searches for any one character except "\n"
to search for "." itself write as \.











. + * ?
\.|\+|\*    [. + * ? \]
"""

"""
m = re.search("Pune\.$",s)
#m = re.search(".",s)
print "m = ", m
if m!=None:
    print m.group()
else:
    print "Match Not found!!!"
print "---------------------------------------------"




"^5$"
"psl|wipro|ibm"
"a|b|c|d"
Character class group
"[abcdefg]"     searching any 1 character
"[a-z]"    

[abc|hello]

"^[0-9]$"


"""
