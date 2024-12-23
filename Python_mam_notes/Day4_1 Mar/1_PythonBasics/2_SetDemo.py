"""

Random/Unordered object: Mutable
Set {}   set()  collection of unique elements
Dictionary {} key:value pairs
"""

s1 = {1, 2, 3, 3, 3, 3}
print("set s1 = ", s1, " type = ", type(s1), " ID = ", id(s1))

s2 = set([3, 3, 4, 5, 6, 6])
print("set s2 = ", s2, " type = ", type(s2), " ID = ", id(s2))

s3 = set([])
# s3 = {[10,20,[1,2,3,4,5]]} #TypeError: unhashable type: 'list'

# print(s1[0])#TypeError: 'set' object is not subscriptable

for i in s1:
    print(i)

print("END")
