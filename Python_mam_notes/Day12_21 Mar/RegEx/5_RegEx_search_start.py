"""regex rule : seraching for the pattern at the beginning"""
import re
s="aaaaaaPSL Welcome to PSL. ^PSL, Pune"   #no match    None
s1="PSLaaaaa Welcome to PSL. PSL, Pune"   #match found
m = re.search("^PSL",s1) 

print ("m = ", m)
if m!=None:
    print ("match content = ", m.group())
else:
    print ("Match Not found!!!")


#1. special Meta characters
#       ^ . + ? * | { }  ( )  [   ]  $
#escape \     "\."   searcing for .
    #\^             searching for ^
#    ^ search at the beginning
#"^pattern"




















"""
"\^"   will search for ^ text character
"^pattern"     will search for the pattern at the beginning of the string

#     ^ $ / \ & * ?  + | [ ] ( ) { } .  these will play a  vital role in RegEx pattern







re.compile("Pune.")   this will match "Pune."   "Pune*"   "Pune "
re.compile("Pune\.")  this will match only "Pune."
"""
