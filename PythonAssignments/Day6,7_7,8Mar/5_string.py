"""
5.	Write a Python program (function) to count the number of strings
where the string length is 2 or more and
the first and last character are same from a given list of strings.
Consider the sample strings in a list as- (['abc','xyz','aba','1221']
"""

list1 = ['abc', 'xyz', 'aba', '1221']
count = 0
for str in list1:
    if (len(str) >= 2):
        if (str[0] == str[-1]):
            count += 1

print("count of valid string : ", count)
