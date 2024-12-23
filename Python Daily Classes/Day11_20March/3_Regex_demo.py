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

"""
Meta Characters : ^ $ . | [ ] { } + * ?
^ -> search at beginning  ---- pattern = "^PSL"
$ -> search at end ---- pattern = "Pune$"
. -> any 1 single char only except \n
| -> match for alternatives "PSL|Infosys|Wipro"
[] -> character class group ---- [abcd] alternative option of single char
                            [a-z],
                            [0-9] ---- Negation [^a-Z]
                            [a-z0-9] ---- Negation [^0-9]
                            [+*?], 
                            [a-zA-Z0-9_] - alphanumeric word char \w
                            [^a-zA-Z0-9_] - Non-alphanumeric word char \W
                            [0-9] digit \d
                            [^0-9] non-digit \D
                            [ \n\t\r] whitespaec \s
                            [^ \n\t\r] Non-whitespace \S

WildCards:
    + 1 or more
    * 0 or more
    ? 0 or 1 only
    "ab*c"    input "abbbbc" match "ac" match "abc" match "abbbbb" - None
    "(ab)+c"

multiple occ
    ab{4}c
    ab{2, 4}c
"""
