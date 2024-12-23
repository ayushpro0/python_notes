s1 = "10:20:30:40"

newlist = s1.split(":")  # [10, 20 ,30 ,40]
print("Original string = ", s1, "type = ", type(s1), " ID = ", id(s1))
print("newlist = ", newlist, "type = ", type(newlist), " ID = ", id(newlist))
# newlist =  ['10', '20', '30', '40'] type =  <class 'list'>  ID =  4440547456

# 1)Get me a new list -numlist  with the elements as int objects from a given list - newlist
numlist = []
for i in newlist:
    numlist.append(int(i))
print("Numlist = ", numlist)

# List Comprehension
# 2) Alternative solution - List comprehension
numlist2 = [int(i) for i in newlist]  # [ 10, 20, 30, 40]
print("Numlist2 = ", numlist2)

# 3) accept these numbers from a keyboard separated by ":" in a line and
# get the int element list input() split() list comprehension

numlist3 = [int(x) for x in input('enter list num elements seperated by :').split(":") if x.isdigit()]
print("Numlist3 = ", numlist3)


"""
enter list num elements separated by :55:66:abc:77:88
Numlist3 =  [55, 66, 77, 88]

"""
print("--------------------------------------------")
list1 = [10, 20, "abc", 30]
squareElements = []
# l = [ int(x)**2 for x in list1 if x.isdigit()]
# AttributeError: 'int' object has no attribute 'isdigit'

squareElements = [x ** 2 for x in list1 if type(x) == int]
print("List1 = ", list1)
print("squareElements = ", squareElements)

print("--------------------------------------------")

# convert only str (only with alphabetical content ) elements into uppercase
words = ["psl", "wipro", 123, "123abcd", "infosys"]
upperwords = [w.upper() for w in words if type(w) == str and w.isalpha()]
print("words = ", words)
print("upperwords = ", upperwords)

"""
words =  ['psl', 'wipro', 'infosys']
upperwords =  ['PSL', 'WIPRO', 'INFOSYS']
"""
