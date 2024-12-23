# You have given a Python list.
# Write a program to find value 20 in the list, and if it is present, replace it with 200.
# Only update the first occurrence of an item.
# Given: list1 = [5,10,15,20,25,50,20] 
# Expected output: [5, 10, 15, 200, 25, 50, 20]


list1 = [5, 10, 15, 20, 25, 50, 20]
print("list1[] : ", list1)

if 20 in list1:
    idx = list1.index(20)
    list1[idx] = 200
    print("Modified list1 : ", list1)

else:
    print("20 is not present in the given list")

# OUTPUT
# list1[] :  [5, 10, 15, 20, 25, 50, 20]
# Modified list1 :  [5, 10, 15, 200, 25, 50, 20]
