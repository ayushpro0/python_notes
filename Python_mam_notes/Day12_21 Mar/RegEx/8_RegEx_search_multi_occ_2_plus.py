import re
#input1 = "xyyyyyyyz"   #match
#input1 = "xyz"         #match
input1 = "xz"           #NO match
#input1 = "xyyyyyyy"    #No match
#input1 = "xyxyzy"      #match
#input1 = "xyxyz"       #match
#input1 = "z"           #NO match
#input1 = "yz"          #NO match

m = re.search("xy+z",input1)  #


print ("m = ", m)
if m!=None:
    print ("Match Content = ", m.group())
else:
    print ("Match Not found!!!")
print ("---------------------------------")

"""
quantifiers
"pattern*"
*   0 or more occurance
+   1 or more
?   0 or 1 only









pattern{num}
pattern{min, max}
pattern{min,}
"""











"""
Accept exact 4 digit number from keyboard, validate

Multiple occurances of a pattern - wild card characters
*     0 or more
+     1 or more
?     0 or 1 only
"pattern*"
{num}          "pattern{4}
{min, max}
{min,}















Ass1:
1.Accept 4 didgit number from user and validate it.
2.Accept a number as a price field
    e.g "$1.55"
    i) should begin with $
    ii) atleast 1 digit after the $ sign
    iii) exact 2 digits after the decimal point






















caharcter class group
a|b|c|d     alternative   [abcd]
[a-z]
Negation group   [^a-z]  search for any 1 character other than a-z

meta characters will behave plainely inside []   [+?*]

[a-zA-Z0-9_]   alphanumeric character class       OR      \w
[^a-zA-Z0-9_]   Non alphanumeric character class    OR    \W
[0-9]           single digit entry                      \d
[^0-9]          Non single digit entry (alphabet/space/meta character)                   \D
[ \n\t\r]       White space                             \s
[^ \n\t\r]      Non White space                             \S


\b         word boundry match
\B         Non word boundry match







"""
















