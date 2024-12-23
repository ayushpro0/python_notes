"""
Python frozenset() Method creates an immutable Set object from an iterable.
It is a built-in Python function.
As it is a set object therefore we cannot have duplicate values in the frozenset.
"""

l = ["Geeks", "for", "Geeks"]

# converting list to frozenset
fnum = frozenset(l)

# printing empty frozenset object
print("frozenset Object is : ", fnum)

print("-------------------------------------")

# creating a dictionary

Student = {"name": "Ankit", "age": 21, "sex": "Male", "college": "MNNIT Allahabad", "address": "Allahabad"}

# making keys of dictionary as frozenset
key = frozenset(Student)

# printing dict keys as frozenset
print('The frozen set is:', key)

print("-------------------------------------")

favourite_subject = ["OS", "DBMS", "Algo"]

# creating a frozenset
f_subject = frozenset(favourite_subject)
print(f_subject)

# below line will generate error
# f_subject[1] = "Networking"
