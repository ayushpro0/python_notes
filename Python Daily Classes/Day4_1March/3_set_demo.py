# Random / Unordered Objects - Mutable
# Set => {} or set() : collection of unique elements
# Dictionary => {} => key:value pairs

 
print("set s1 = ", s1, " type = ", type(s1), "ID = ", id(s1))
# set s1 =  {1, 2, 3}  type =  <class 'set'> ID =  1740019111232

s2 = set([3, 3, 4, 5, 6, 6])
# set s2 =  {3, 4, 5, 6}  type =  <class 'set'>  ID =  1740019110560

# s3 = {[10, 20, [1, 2, 3, 4, 5]]} # TypeError: unhashable type: 'list'

# create empty set
s4 = set([])
print("set s4 = ", s4, " type = ", type(s4), " ID = ", id(s4))
# set s4 =  set()  type =  <class 'set'>  ID =  2391984149600

# print(s1[0]) # TypeError: 'set' object is not subscriptable

for i in s1:
    print(i)

print("END")


