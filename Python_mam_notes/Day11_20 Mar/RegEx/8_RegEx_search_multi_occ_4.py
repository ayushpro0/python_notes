import re

# input1 = "xyyyyz"          #match
# input1 = "xyyz"            #match
input1 = "xyyyyz"  # match
# input1 = "xyyyyyyyz"       #No match
# input1 = "xyz"             #NO match

m = re.search("xy{2,4}z", input1)  #

print("m = ", m)
if m != None:
    print("Match Content = ", m.group())
else:
    print("Match Not found!!!")
print("---------------------------------")
"""
Take an input from keyboard for 2 digit number only (00-99). pattern to validate this


#keyboard input for price field in $
1. shd begin with $
2. after $ , there shd atleast 1 digit
3. after 1 or more digits . decimal must
4. after decimal point , exact 2 digits only
eg.
$1.55       valid
$55.66nvghvh      valid
$.67        NOt valid
$567.8      NOT valid
"""

"^\$\d+\.\d{2}$"

# . matches any 1 single char alphabet digit spc char any space but except \n


"""
quantifiers
"pattern*"
*   0 or more occurance
+   1 or more
?   0 or 1 only


pattern{num}
pattern{min, max}
pattern{min,}






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
