'''1.	Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write Python code that takes this list a and makes a new list b that has only the even elements of this list in it. 
'''
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []
for i in a:
    if i%2 == 0:
        b.append(i)

print("Even list: ",b)