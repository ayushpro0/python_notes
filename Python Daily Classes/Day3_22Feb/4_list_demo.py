
list1 = [10, 20, 30, 40]
print("list1 = ", list1, " Type = ", type(list1), " ID = ", id(list1))
# list1 =  [10, 20, 30, 40]  Type =  <class 'list'>  ID =  2619253216448

list1.append(50)
print("list1 = ", list1) # list1 =  [10, 20, 30, 40, 50]

list1.append([55, 66]) # adds list as object inside list1
print("list1 = ", list1) # list1 =  [10, 20, 30, 40, 50, [55, 66]]

list1.extend([99, 88]) # adds 99 and 88 as seperate elements
print("list1 = ", list1) # list1 =  [10, 20, 30, 40, 50, [55, 66], 99, 88]

print("--------------------------------------------")

list2 = [99, 88, 10, 33, 555, 345, 199, 5678]
print("list2 = ", list2, " Type = ", type(list2), " ID = ", id(list2))
# list2 =  [99, 88, 10, 33, 555, 345, 199, 5678]  Type =  <class 'list'>  ID =  2258246924160

list2.sort()
print("Ascending Sorted list2 = ", list2, " Type = ", type(list2), " ID = ", id(list2))
# Ascending Sorted list2 =  [10, 33, 88, 99, 199, 345, 555, 5678]  Type =  <class 'list'>  ID =  2258246924160

list2.sort(reverse = True)
print("Descending Sorted list2 = ", list2, " Type = ", type(list2), " ID = ", id(list2))
# Descending Sorted list2 =  [5678, 555, 345, 199, 99, 88, 33, 10]  Type =  <class 'list'>  ID =  2258246924160

print("--------------------------------------------")

# list2 = [99, 88, 10, 33, 555, "abc", 345, 199, 5678]
# list2.sort() # TypeError: '<' not supported between instances of 'str' and 'int'

print("--------------------------------------------")

words = ["xyz", "abc", "bob", "lmn"]
print("words = ", words, " Type = ", type(words), " ID = ", id(words))

words.sort()
print("Ascending Sorted words = ", words, " Type = ", type(words), " ID = ", id(words))

# words =  ['xyz', 'abc', 'bob', 'lmn']                     Type =  <class 'list'>  ID =  1799497873280
# Ascending Sorted words =  ['abc', 'bob', 'lmn', 'xyz']    Type =  <class 'list'>  ID =  1799497873280

# check the followin methods =>
    # list.reverse
    # list.pop
    # list.insert

    