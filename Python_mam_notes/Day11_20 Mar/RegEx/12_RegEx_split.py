"""
s = "ABC:XYX:lmn:hghg"
l1 = s.split(":")    ["ABC" , "XYZ"]
"""
# What is the size of below list1 created after re.split() call?
import re

s = 'str1:str2:str3'
list1 = re.split(':', s)
print("list1 =", list1)

print("len (list1) = ", len(list1))  # 3

print("----------------------------------")

s2 = 'str1:str2*str3?str4'
list2 = re.split('[*?:]', s2)
# * & + wildcards  search("")  [0-9]   [abcd]  "\*|\?|:"  ['str1', 'str2', 'str3', 'str4']
print("list2 = ", list2)
print("len (list2) = ", len(list2))  # 4
print("----------------------------------")

s3 = 'str1:str2;str3---str4,str5'
list4 = re.split('[:;,]|---', s3)
# list4 = re.split('[:;,---]', s3)
print("list4 = ", list4)  # list4 =  ['str1', 'str2','str4', 'str5']
print("----------------------------------")

s = "This is jus testing. This is aa123bb just testing.This is just testing"
target_list = []  # containing only lower case alphabetical words
res = re.split("\s+", s)  # list of all words
# target_list = [i for i in res if re.search("^[a-z]+$", i)!=None]
target_list = [i for i in res if re.search("^[a-z]+$", i)]
print("Target1 =", target_list)

"""















pattern = r'\d'
s3= 'str1:str2*str3?str4'
list3 = re.split(pattern, s3)     #['str', ':str', '*str', '?str', '']
print list3
print "----------------------------------"



"""

"""

s = "This is jus testing. This is aa123bb just testing.This is just testing"
res = re.split("\s+", s)     #list of all words
print "res = ",res
target = []                 #which will contain only lower alphabetical words from this list
for i in res:
    match1 =re.search("^[a-z]+$", i)
    if match1!=None:
        target.append(i)
print "Original List = ", res
print "Target = ", target
print "----------------------------------------------"
res = re.split("\s+", s)     #list of all words
target1 = [i for i in res if re.search("^[a-z]+$", i)!=None]
print "Target1 =", target1





Read the content of  a file . Print the count of word "Persistent"
print "-------------------------------------------------------------------"
fh = open("data.txt")
words = []
for line in fh:
    words.extend([i for i in re.split("\s+", line) if re.search("^Persistent$",i)!=None])
print "Count of word =", len(words)

print "-------------------------------------------------------------------"
                 
"""
