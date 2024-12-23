import re

s1 = "Welcome to PSL. PSL in Pune"
matchObj = re.search("psl", s1)
print("matchObj = ", matchObj)# None
print("----------------------------------------------")


matchObj = re.search("psl", s1, re.IGNORECASE)
print("matchObj = ", matchObj)#
#<re.Match object; span=(11, 14), match='PSL'>
print("----------------------------------------------")

if matchObj != None:
    print("match obtained  = ", matchObj)
    print("Match Content is = ",matchObj.group() )
else:
    print("Match Not found!!!!")
