import re

# num = raw_input("Enter 4 digit number :")  #in Python 2.x
num = input("Enter number :")  # in Python 3.x

m = re.search("\d{4}", num)  # is it the precise pattern to validate exact 4 digit number entry from user???

print("m = ", m)
if m != None:
    print("match content = ", m.group())
else:
    print("Match Not found!!!")
print("---------------------------------------------")

"""
{num}
{min,max}
{min,}

[a-z]
[^a-z]
"\*|\?|\."
[*?.]   all meta characters behave plainly inside []
"[*?.]|-{3}"
"[*?.]"

"[^0-9]"  negation of that character class group, it will give match to alphabet or any 1 special charcter or white space \n \t \r \f 
"^psl"
[^abcd]
[0-9]                                                   \d    searches for any 1 single digit
[^0-9] negation                                         \D    searches for any 1 single NON-digit entry
[a-zA-Z0-9_]   alphanumeric word character              \w    searches for any 1 single alphanumeric word character
[^a-zA-Z0-9_]  Non alphanumeric word character          \W    searches for any 1 single NON alphanumeric word character
[ \n\t\r\f]    white space                              \s
[^ \n\t\r\f]   NON white space                          \S
                                                        \b    search by word boundry
                                                        \B    search by NON word boundry
"""

"""

"\bpsl\b"
"\s+"
"""
