import re

s1 = "Welcome to PSL. PSL in Pune"

matchObj = re.search("psl", s1)
print("matchObj = ", matchObj)  # matchObj =  None

print("--------------------------------------------")

matchObj = re.search("psl", s1, re.IGNORECASE)
print("matchObj = ", matchObj)  # matchObj =  <re.Match object; span=(11, 14), match='PSL'>

print("--------------------------------------------")

if matchObj is not None:
    print("match obtained = ", matchObj)
    print("Match Content is = ", matchObj.group())  # Match Content is =  PSL
else:
    print("Match Not found !!!")
