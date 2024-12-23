
# Take a input string with words seperated by a space
# example: "abc xyz abc123 LMN AAAA 555"
# Extract only UpperCase aplhabetical words only in a newUpperList
# Expected O/P: 
    # newUpperList = ["LMN", "AAAA"]

import re

s = "abc xyz abc123 LMN AAAA 555 AAAA123,BBB"

# Solution 1
pattern = r'\b[A-Z]+\b' # find all capital letter words, 
# it will fail for "AAAA123,BBB" becasue \b can be either space, comman, colon, etc, word boundary
newUpperList = re.findall(pattern, s)

print("NewUpperCase word list = ", newUpperList) # ['LMN', 'AAAA']

print("------------------------------------------")


list1 = ["abc", "xyx", "abc123", "LMN", "AAAA", 555, "BBBB123", 3.14, [1,2,3,4]]

# using list comprehension
new_upper_list = [w for w in list1 if type(w) == str and w.isalpha() and  w.isupper()]

print("new upper list = ", new_upper_list) # ['LMN', 'AAAA']

print("------------------------------------------")

# using REGEX
new_upper_list2 = [w for w in list1 if type(w) == str and re.search("^[A-Z]+$", w)]
print("new upper list = ", new_upper_list2) # ['LMN', 'AAAA']
