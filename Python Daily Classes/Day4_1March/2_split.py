# split() - return an list 

s1 = "10:20:30:40"
newlist = s1.split(":") #  [10, 20, 30, 40]

print("Original String : " , s1, "type = ", type(s1), "ID = ", id(s1))
print("newlist : ", newlist, "type = ", type(newlist), "ID = ", id(newlist))

# Original String :  10:20:30:40 type =  <class 'str'> ID =  2276476800944
# newlist :  ['10', '20', '30', '40'] type =  <class 'list'> ID =  2276476801536
# uppar wala abhi bhi string hai, int nahi bana abhi tak


# 1. Get me a new list -numlist with the elements as int objects from a given list-newlist

numlist = []
for i in newlist:
    numlist.append(int(i))
print("Numlist : ", numlist) # Numlist :  [10, 20, 30, 40]

# 2. Alternative Solution -> List Comprehension

numlist2 = [int(i) for i in newlist] # [10, 20, 30, 40]
print("Numlist2 : ", numlist2) # Numlist2 :  [10, 20, 30, 40]

#--------------------------------------------------------------------------------------------------

# 3. accept these numbers from keyboard seperated by ":" in a line and get the int element list
# input() -> split() -> list comprehension

numlist3 = [int(x) for x in input('enter list num elements seperated by :').split(":")]
print("Numlist3 = ", numlist3)

# input -> 11:22:33:44:55
# output -> Numlist3 =  [11, 22, 33, 44, 55]

# input -> 55:66:77:abc:65 
# output -> ValueError: invalid literal for int() with base 10: 'abc'

#--------------------------------------------------------------------------------------------------

# modified the upar wala to accept int and ignore string elements
# numlist4 = [int(x) for x in input('enter list num elements seperated by :').split(":") if x.isdigit()]
# print("Numlist4 = ", numlist4) 

# input -> :10:abc:30:40
# output -> Numlist4 =  [10, 30, 40]

print("----------------------------------------------------")

list1 = [10, 20, "abc", 30]
squareElements = []

# l = [ int(x)**2 for x in list1 if x.isdigit()]
# AttributeError: 'int' object has no attribute 'isdigit'

# solution is to check the type of the element is "int" or not
squareElements = [x**2 for x in list1 if type(x) == int]
print("List1 = ", list1) # List1 =  [10, 20, 'abc', 30]
print("squareElements = ", squareElements) # squareElements =  [100, 400, 900]

print("----------------------------------------------------")

words = ["psl", "wipro", "infosys"]
print("words = ", words) # words =  ['psl', 'wipro', 'infosys']

upperwords = [ w.upper() for w in words ]
print("upperwords = ", upperwords) # upperwords =  ['PSL', 'WIPRO', 'INFOSYS']

print("----------------------------------------------------")

# inserting a "int" value in string list to change it to uppercase
words1 = ["psl", "wipro", 123, "123abcd", "infosys"]
print("words1 = ", words1) # words1 =  ['psl', 'wipro', 123, '123abcd', 'infosys']

# upperwords1 = [w.upper() for w in words1] # "int" value will not be change in UpperCase and give out error
# print("upperwords1 = ", upperwords1) # AttributeError: 'int' object has no attribute 'upper'

# to ignore the "int" value, we check the type of every element, and only select the "str" values
# ignore "int" value like 123
upperwords1 = [w.upper() for w in words1 if type(w) == str]
print("upperwords1 = ", upperwords1) # upperwords1 =  ['PSL', 'WIPRO', '123ABCD', 'INFOSYS']


# convert only str (only with alphabetical content) element into UPPERCASE
# we also need to ignore "123abcd"
upperwords2 = [w.upper() for w in words1 if type(w) == str and w.isalpha()]
print("upperwords2 = ", upperwords2) # upperwords2 =  ['PSL', 'WIPRO', 'INFOSYS']

print("----------------------------------------------------")