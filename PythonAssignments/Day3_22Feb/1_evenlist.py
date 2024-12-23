# 1. Let’s say I give you a list saved in a variable: 
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
# Write Python code that takes this list a and makes a new list b that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []
for element in a:
    if element % 2 == 0:
        b.append(element)

print("A[] : ", a)
print("B[] : ", b)

# OUTPUT:
# A[] :  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# B[] :  [4, 16, 36, 64, 100]
