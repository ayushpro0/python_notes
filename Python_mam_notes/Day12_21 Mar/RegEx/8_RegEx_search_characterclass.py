"""character class group : []   eg [abcdef]   [Pune|PSL]"""
import re
#input1 = "999"# 1 alphabet followed with one digit only    s9   q6     aa1   qq45

s="PSL Welcome to PSL. PSL, Pune + aaa2015bbb"
m = re.search("[abcd]",s)    #c
#m = re.search("[a-zA-Z]",s)    #P
#m = re.search("[^a-zA-Z]",s)    #space
#m = re.search("[0-9]",s)    #2
#m = re.search("[^0-9]",s)    #P
#m = re.search("\d",s)    #2
#m = re.search("\D",s)    #P

print ("m = ", m)
if m!=None:
    print ("Match Content = ", m.group() )   #
else:
    print ("Match Not found!!!")
print ("---------------------------------")

\s   single space

"""
+ one or more     "\s+"   re.split("\s+", str1) str1="abc\nvbv\tbvgv    lmn"   =["abc","vbv","bvg","lmn"]
*
?
"""






"""
character class group
a|b|c|d             ----->    "[abcd]"
[a-z]
[a-zA-Z]
[+?*|]        these meta characters behave plain inside [^]
[^a-zA-Z]
[0-9]           ------->              \d
[^0-9]           ------->              \D
[a-zA-Z0-9_]    alphanumeric word character   \w
[^a-zA-Z0-9_]    alphanumeric word character   \W
[ \n\t\r]   white spaces                            \s
                                                    \s+
[^ \n\t\r]   white spaces                            \S
                                                    

"""
























































"""
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



#m = re.search("[a-z]",s)       #   match is "e"
#m = re.search("[a-zA-Z]",s)    #   match is "P"
#m = re.search("[0-9]",s)       #   match is "2"
#m = re.search("[^a-z]",s)      #   match is "P"
#m = re.search("[a-zA-Z0-9]",s)  #   match is "P"
#m = re.search("\d",s)  #   match is "2"
#m = re.search("\D",s)  #   match is "P"
m = re.search("^[a-zA-Z]\d$",input1)  #   match is "A1"




"""
















