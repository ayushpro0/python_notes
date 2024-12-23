# Updating List data:
# Example :Replacing a value in List,
# Functions - append, insert, remove pop

listOne = [100, 200, 'hello']  # List definition with different data objects, List is mutable
print("listOne = ", listOne)  # listOne =  [100, 200, 'hello']

# print ("List element at 5 index = ", listOne[5]) # IndexError: list index out of range

listOne[2] = 200  # Replacing a value in List at index 2
print("After index assignment = ", listOne)  # After index assignment =  [100, 200, 200]

print("---------------------------------------------------------------")

print(dir(listOne))

print("---------------------------------------------------------------")

listOne.append(500)  # append function to append a value
print("After appending 1 value = ", listOne)  # After appending 1 value =  [100, 200, 200, 500]

listOne.append([600, 700])  # append function to append a list
print("After appending inner list = ", listOne)  # After appending inner list =  [100, 200, 200, 500, [600, 700]]

print("-----------------------------------------------")

listThree = [123, 'abc', 4.56, 4.56]  # insert function to insert value in a list
listThree.insert(2, 'c')  # insert 'c' at 2nd index

print("List after insert =", listThree)  # List after insert = [123, 'abc', 'c', 4.56, 4.56]

listThree.insert(-1, 666)  # insert 666 at the last index of the list
print("List after insert = ", listThree)  # List after insert = [123, 'abc', 4.56, 666, 4.56]

# remove(x) function

listThree.remove(4.56)  # removes the first occurrence of the given value
print("List after remove = ", listThree)  # List after remove =  [123, 'abc', 'c', 666, 4.56]

# listThree.remove(4)  #remove function to remove a value from a list
# ---ValueError: list.remove(x): x not in list

print("--------------------------------------------------")

# pop() function
listSix = [123, 'abc', 4.56]  # pop function to remove last element
print("popped element as return value of pop function = ", listSix.pop())
# popped element as return value of pop function =  4.56

print("Modified List after pop =", listSix)  # Modified List after pop = [123, 'abc']

# pop(index) -> to remove element present at the given index
listSix.pop(1)  # pop function call removing element at index 1 i.e. 'abc'

# listSix.pop(5) #run time error as index 5 not existing

print("Modified List =", listSix)  # Modified List = [123]

print("Count of 123 = ", listSix.count(123))  # Count of 123 =  1

print("Count of ListSix list elements = ", len(listSix))  # Count of ListSix list elements =  1
