# pass a list as parameter, square all the elements inside the function
# and cross verify if the original list is modified

def testing(list1):
    print('Inside function ...')
    print("list1 = ", list1, " ID = ", id(list1))
    list1.append(9999)

    # list1 = [i**2 for i in list1] # this will not change phle wala list1, ye ek naya "list1" naam ka list banayega
    # print("list1 = ", list1, " ID = ", id(list1))

    for i in range(len(list1)):
        list1[i] = list1[i]**2
    print("list1 = ", list1, " ID = ", id(list1))




print("Calling testintg")

num1 = [10, 20,30, 40]
print('original num1 = ', num1, " ID = ", id(num1))
print("-----------------------------------------")
testing(num1)
print("-----------------------------------------")
print("num1 after testing fun call = ", num1, " ID = ", id(num1))