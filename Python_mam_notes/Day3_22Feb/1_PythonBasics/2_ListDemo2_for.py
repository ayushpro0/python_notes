"""
List / tuple def, slicing
"""
# list def
list1 = [10, 20, 30, 40]
squarelist = []

print("list1 = ", list1, " Type = ", type(list1), " ID = ", id(list1))
# list1 =  [10, 20, 30, 40]  Type =  <class 'list'>  ID =  2969079338048

ans = sum(list1)
print("addition of list1 elements = ", ans)  # addition of list1 elements =  100

for i in list1:  # i gives element value
    print(i)
    i = i ** 2
    squarelist.append(i)

print("list1 = ", list1)  # list1 =  [10, 20, 30, 40]  Type =  <class 'list'>  ID =  2969079338048

print("squarelist = ", squarelist)  # squarelist =  [100, 400, 900, 1600]

print("----------------------------------------------------------------------")

# want to an index and an element also : for + range
# Task: change every element to square value in the original list itself

for i in range(len(list1)):  # len(list1) ->4  range(4) -> 0,1,2,3
    print("Index = ", i, " Element = ", list1[i])
    # list1[i] = list1[i]**2
    list1[i] **= 2

print("list1 = ", list1, " ID = ", id(list1))
# list1 =  [100, 400, 900, 1600]  Type =  <class 'list'>  ID =  2969079338048


# list1.append[i]=i**2
