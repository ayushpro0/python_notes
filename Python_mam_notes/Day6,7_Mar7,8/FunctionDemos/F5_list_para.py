def testing(list1):
    print("Inside function.....")
    list1.append(9999)
    print("list1 =   ", list1, " ID = ", id(list1))
    # list1 = [i**2 for i in list1 ]
    # print("list1 =   ", list1, " ID = ", id(list1))
    for i in range(len(list1)):
        list1[i] = list1[i] ** 2  # will it change num1 list???


print("Calling testing.....")
num1 = [10, 20, 30, 40]
print("Original num1 = ", num1, " ID = ", id(num1))

print("---------------------------------------------------")

result = testing(num1)

print("---------------------------------------------------")

print("num1 after testing fun cal = ", num1, " ID = ", id(num1))
print("result = ", result)
