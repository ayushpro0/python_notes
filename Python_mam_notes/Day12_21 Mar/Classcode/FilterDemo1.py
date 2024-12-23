
# 1
list1 =[10, 20, 30, 40, 50]
lessthan30 = [i for i in list1 if i < 30]
print("list1 = ", list1)
print("lessthan30 = ", lessthan30)  # [10, 20]

print("---------------------------------------")


# 2)alternative sol to above list comprehension

def test(x):
    return x < 30


filterObj = filter(test, list1)
print("filterObj = ", filterObj)  # <filter object at 0x108e52e60> -> 10 20
print("Filtered list = ", list(filterObj))
