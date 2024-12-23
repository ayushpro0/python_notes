"""1.	Create a text file “emails.txt” and
store a big list of valid and invalid email addresses on separate lines.
Write a program to match the set of all valid e-mail addresses."""

import re

file1 = open("emails.txt", 'r')
cont = file1.readlines()
li = []
pat = r'^[a-z0-9]+@[a-z]+\.[a-z]{2,3}$'

for mail in cont:
    # print(mail)
    if re.search(pat, mail):
        li.append(mail)

print('\n'.join(li))
