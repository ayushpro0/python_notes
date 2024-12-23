

# filter 
#1
list1 = [10, 20, 30, 40, 50]

lessthan30 = [i for i in list1 if i < 30]
print("list1 = ", list1)
print("listthan30 = ", lessthan30) # [10, 20]

print("--------------------------------------------")

#2. alternative solution to about list comprehension
def test(x):
    return x < 30

filterObj = filter(test, list1)
print("filterObj = ", filterObj) # <filter object at 0x0000017B4A42B970>

print("Filtered List = ", list(filterObj)) # [10, 20]

print("--------------------------------------------")

filterObj = filter(lambda x : x < 30, list1)
print("Filtered List = ", list(filterObj))