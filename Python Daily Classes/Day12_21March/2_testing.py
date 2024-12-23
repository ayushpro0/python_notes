# validate input to be exact 3 digit entry number
import re

s = input("Enter the digits: ")
pattern = r"^\d{3}$"

m = re.search(pattern, s)

print("m = ", m)

if m != None:
    print("Match content = ", m.group())
else:
    print("Match Not Found")
