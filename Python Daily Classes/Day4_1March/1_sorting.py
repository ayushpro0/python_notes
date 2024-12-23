nums = [100, 56, 2, 9999]
print("Original List : ", nums) # Original List :  [100, 56, 2, 9999]


# list.sort() - original list is sorted
nums.sort() # ye wala sort() list ka khudka hai
print("Sorted elements : ", nums)  # Sorted elements :  [2, 56, 100, 9999]

nums.sort(reverse = True)
print("Reversed Sorted elements : ", nums) # Reversed Sorted elements :  [9999, 100, 56, 2]

words = ['Aaaa', 'bb', 'ccccccc', 'zzzzzzzzzzz']

words.sort() # Default sorting Ascending | this is InPlace Sorting
print("Words Default Sorted : ", words) # Words Default Sorted :  ['Aaaa', 'bb', 'ccccccc', 'zzzzzzzzzzz']

words.sort(key = len) # Functional Programming len(words[0]) -> 4 len(words[1]) -> 2
print("Words sorted by len : ", words) # Words sorted by len :  ['bb', 'Aaaa', 'ccccccc', 'zzzzzzzzzzz']

print("-------------------------------------------")

# Sorted Function - it is a general function
# sorted(l1) => this function return a new sorted list
l1 = [23, 10, 6, 99]
sortedl1 = sorted(l1) 
print("Original l1 : ", l1) # Original l1 :  [23, 10, 6, 99]
print("Sorted l1 Increasing : ", sortedl1) # Sorted l1 Increasing :  [6, 10, 23, 99]

sortedl1_rev = sorted(l1, reverse = True) # keyword argument passing
print("Reverse Sorting : ", sortedl1_rev) # Reverse Sorting :  [99, 23, 10, 6]

print("-------------------------------------------")


# list.reverse() => original list is reversed

num1 = [10, 20, 30, 40]
rev_Obj = reversed(num1) # this will return an ReverseObject, ye object list nahi hai usko list banana padega
print("Num1 = ", num1)
print("Revered List = ", rev_Obj) # <list_reverseiterator object at 0x0000021A2F58BF70>
rev_num1 = list(rev_Obj)
print("Reverse List = ", rev_num1) # [40, 30, 20, 10]

print("-------------------------------------------")

newTuple = tuple(num1) # list num1 getting converted into a Tuple
print("num1 = ", num1, "type = ", type(num1)) # num1 =  [10, 20, 30, 40] type =  <class 'list'>
print("newTuple = ", newTuple, "type = ", type(newTuple)) # newTuple =  (10, 20, 30, 40) type =  <class 'tuple'>

print("-------------------------------------------")

# "pass" command - to pass the control to the next block 

n1 = 101
if n1 == 100:
    pass
elif n1 == 99:
    pass
else : print("else block")