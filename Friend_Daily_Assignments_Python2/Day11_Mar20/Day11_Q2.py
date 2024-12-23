"""2.	Create a text file “urls.txt” and store a big list of  URLs.
Write a program to match simple Web domain names that begin with
"www." and end with a ".com" suffix, e.g., http://www.yahoo.com. """

import re
file1 = open("URLs.txt", "r")
content = file1.readlines()
#li = []
pat = r'www\.[a-z0-9]+\.com'

for url in content:
    if re.search(pat, url):
        print(url)




