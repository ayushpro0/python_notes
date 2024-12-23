# string data access : immutable

s1 = "012345"
print("s1 = ", s1, "type = ", type(s1))  # 012345
print("s1[0] = ", s1[0])  # 0
print("s1[-1] = ", s1[-1])  # 5
print("s1[2:4] = ", s1[2:4])  # 23
print("s1[:4] = ", s1[:4])  # 0123
print("s1[3:] = ", s1[3:])  # 345

print("s1[-5:-2] = ", s1[-5:-2])  # 123
print("s1[-2:-4] = ", s1[-2:-4])  # blank o/p


# s1 = "012345"
print("s1[::-1] = ", s1[::-1])  # traversal direction specified - 543210
print("s1[::2] = ", s1[::2])  # 024
print("s1[-5:-2:-1] = ", s1[-5:-2:-1])  # blank o/p
print("s1[-2:-5:-1] = ", s1[-2:-5:-1])  # 432

print("s1.isdigit() = ", s1.isdigit())  # True

s2 = "persistent"
upperstr = s2.upper()
print("s2 = ", s2)  # persistent
print("upperstr = ", upperstr)  # PERSISTENT
print("-" * 45)

# Immutability
str1 = "Hello "
print("str1 = ", str1, "type = ", type(str1), " ID = ", id(str1))

str1 = str1 + " World!"
print("str1 = ", str1, "type = ", type(str1), " ID = ", id(str1))

print("-" * 45)

num1 = 10
num2 = 20
ans = num1 + num2
print("num1 =%d num2 = %d Addition = %d" % (num1, num2, ans))

print("num1 = %d  num2 = %d addition = %d " % (num1, num2, num1 + num2))

print("-" * 45)

s1 = "PSL"
size = len(s1)
print("len of s1 = ", size)

for i in s1:
    print(i)

rangeobj = range(3)  # 0 1 2
print("rangeobj = ", rangeobj)  # range(0,3)

list1 = list(rangeobj)
print("list1 = ", list1)  # [0, 1, 2]

for i in range(3):
    print(i)
