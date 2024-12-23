# string data access

s1 = "012345"

print("s1 = ", s1, "type = ", type(s1))  # 012345 - <class 'str'>

print("s1[0] = ", s1[0])  # 0

print("s1[-1] = ", s1[-1])  # 5

print("s1[2:4] = ", s1[2:4])  # 23

print("s1[:4] = ", s1[:4])  # 0123

print("s1[3:] = ", s1[3:])  # 345

print("s1[-5:-2] = ", s1[-5:-2])  # 123

print("s1[-2:-4] = ", s1[-2:-4])  # blank O/P

print("s1[::-1] = ", s1[::-1])  # 543210 - traversal direction specified

print("s1[::2] = ", s1[::2])  # 024 - +ve direction & 2 increment

print("s1[-5:-2:-1]", s1[-5:-2:-1])  # blank output

print("s1[-2:-5:-1] = ", s1[-2:-5:-1])  # 432 - because the index & direction is matching

print("s1.isdigit()", s1.isdigit())  # True

print("---------------------------------------------------")

s2 = "persistent"

upperstr = s2.upper()

print("s2 = ", s2)  # persistent
print("upperstr = ", upperstr)  # PERSISTENT

print("-------------------------------------------------------")

# Immutability

str1 = "Hello "
print("str1 = ", str1, "type = ", type(str1), "ID = ", id(str1))

str1 = str1 + "World!"
print("str1 = ", str1, "type = ", type(str1), "ID = ", id(str1))

print("-------------------------------------------------------")

# Formatting
num1 = 10
num2 = 20
print("num1 = %d num2 = %d Addition = %d" % (num1, num2, num1 + num2))

print("---------------------------------------------------------")


s1 = "PSL"
size = len(s1)
print("len of s1 = ", size)

# For loop
for i in s1:
    print(i)

rangeobj = range(3)  # 0 1 2
print("rangeobj = ", rangeobj, " type: ", type(rangeobj))  # range(0,3)



list1 = list(rangeobj)
print("list1 = ", list1)  # [0, 1, 2]

for i in range(3):
    print(i)


#--------------
s44 = "Ayush Kumar Giri"
for ch in s44:
    print(ch)

for i in range(len(s44)):
    print(s44[i])
