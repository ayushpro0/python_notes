"""search by ignoring the case"""
import re

s = "Welcome to aaaaaapsl. persistent......"

regex = re.search("PSL", s, re.IGNORECASE)  # , re.IGNORECASE
print("regex object = ", regex)

if regex != None:
    print("Match Found = ", regex.group())  # psl
else:
    print("Match Not found!!!")

"""
re Flags
re.IGNORECASE makes the pattern case insensitive so that it matches strings of different capitalizations
re.MULTILINE is necessary if your input string has newline characters (\n) and allows the start and end metacharacter
(^ and $ respectively) to match at the beginning and end of each line instead of at the beginning and end of the whole
input string
re.DOTALL allows the dot (.) metacharacter match all characters,
including the newline character (\n)

"""
