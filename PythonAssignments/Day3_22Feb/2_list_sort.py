# 2.	List sorting sort the list of following names by –
#           - an ascending order of words
#           - descending order of words
#           - an ascending order of number of letters in each name 
# unsortedList = ['Aaaa', 'bb', 'cccccccc', 'zzzzzzzzzzzz']

unsortedList = ['Aaaa', 'bb', 'cccccccc', 'zzzzzzzzzzzz']

# ascending order
unsortedList.sort()
print("Ascending Order : ", unsortedList)

# descending order
unsortedList.sort(reverse=True)
print("Descending Order : ", unsortedList)

# sorting based of length of each element
unsortedList.sort(key=len)
print("Length based Sorting : ", unsortedList)

# OUTPUT
# Ascending Order :  ['Aaaa', 'bb', 'cccccccc', 'zzzzzzzzzzzz']
# Descending Order :  ['zzzzzzzzzzzz', 'cccccccc', 'bb', 'Aaaa']
# Length based Sorting :  ['bb', 'Aaaa', 'cccccccc', 'zzzzzzzzzzzz']
