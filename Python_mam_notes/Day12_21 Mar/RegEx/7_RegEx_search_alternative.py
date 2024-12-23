
import re
s="*\n Welcome to PSL. PSL, Pune"

#m = re.search("Pune|PSL",s)    # | is alternative  PSL, whichever found first is a match
m = re.search("Pune|^PSL",s)    # | is alternative  PSL, whichever found first is a match
print ("m = ", m)
if m!=None:
    print (m.group())   #PSL
else:
    print ("Match Not found!!!")
print ("---------------------------------------------")


"""
|   alternative search   - for this use | meta character
"patt1|patt2 |patt3"








****character class group by using []
"a|b|c|d"      ------>   [abcd]
#[Pune|PSL]   all metacharacters play as normal except ^
[a-z]
[a-zA-Z]
[0-9]                   -----> \d    digit search
[^0-9]   negation       -----> \D    NON-digit  -alphabets, spc chr, spaces
[a-zA-Z0-9_] alphanumeric word caharacter   \w
[^a-zA-Z0-9_] non alphanumeric word caharacter   \W spc char, spaces
[ \n\t\r]     white space \s
[^ \n\t\r]     white space \S

***Wild cards
*   0 or more
+   1 or more
?  0 or 1 only
"pattern_char*"











































"""
