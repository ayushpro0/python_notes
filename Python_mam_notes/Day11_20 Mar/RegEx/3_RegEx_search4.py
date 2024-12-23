
import re

s = "xyyyyyyyyghg"
m = re.search("xy{2,}", s)  # + * ?   +  1 or more   * 0 or more  ? 0 or 1 only    \b is word boundry

print("m = ", m)

if m != None:
    print("Match Found = ", m.group())
else:
    print("Match Not found!!!")

# search anywhere first occurrence only

"""
re  metacharacters
.  any 1 character except \n
^   search at the beginning
$  search at the end
|  alternative
( ) group
"."
"^PSL"
"PSL\$"
"PSL|WIPRO|IBM"
"(PSL) (PUNE)"
"(\d+)"
    1  2
    match(0)   entire match
match(1)
match(2)
xy{num}
"xy{2}z"   xyyz yes     xyyyyyz   No
   XZ  no

xy{min, max}
xy{2,4}z
"""
