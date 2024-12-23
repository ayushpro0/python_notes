import re

s1 = "Welcome to PSL. PSL in Pune"
if s1.find("PSL"): print("PSL found in S1")
else:print("PSL not found!!!")
print("------------------------------------------------")

matchObj = re.match("PSL", s1)
print("matchObj = ", matchObj)#None

s2 = "PSL Welcome to PSL. PSL in Pune"
matchObj = re.match("PSL", s2)
print("matchObj = ", matchObj)#<re.Match object; span=(0, 3), match='PSL'>
print("------------------------------------------------")

matchObj = re.search("PSL", s1)
print("matchObj = ", matchObj)

print("matchObj = ", matchObj)#None

