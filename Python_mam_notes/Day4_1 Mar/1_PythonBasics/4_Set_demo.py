"""Set definition"""

s1 = {1, 2, 3, 3, 3, 3}  # st is unordered , no duplicate values allowed
print("set s1 = ", s1)  # {1, 2, 3}

print("-------------------------------------")

list1 = [10, 22, 33, 33]
s2 = set(list1)
print("set s2 = ", s2)  # {33, 10, 22}

# print ("s1 element = ", s1[0])  #TypeError: 'set' object does not support indexing

s2 = {}  # is it empty set??? ---NO
print("type of s2 = ", type(s2))  # <class 'dict'>

s22 = set([])  # empty set
print("type of s22 = ", type(s22))  # <clas 'set'>
print("-------------------------------------")

s3 = set([1, 2, 3])
s4 = set([3, 4, 5, 6])

# set Union
setNew1 = s3 | s4
print("Orginal set s3 = ", s3)  # {1, 2, 3}
print("Orginal set s4 = ", s4)  # {3, 4, 5, 6}
print("New Union set = ", setNew1)  # {1, 2, 3, 4, 5, 6}

print("-------------------------------------")

# set intersection
setNew2 = s3 & s4
print("Orginsl set s3 = ", s3)  # {1, 2, 3}
print("Orginsl set s4 = ", s4)  # {3, 4, 5, 6}
print("New intersection set = ", setNew2)  # {3}

# ============================================================


# s44 = {3,2,1,[11,22,33]}  #???
# print "set s44 = ", s44  #TypeError: unhashable type: 'list'

"""
s3 = set([1,2,3])
it = iter(s3)
print ("set element = ", it.next())
print ("set element = ", it.next())
print ("set element = ", it.next())
#print ("set element = ", it.next())  #StopIteration
print ("len of set s3 = ", len(s3))

"""
