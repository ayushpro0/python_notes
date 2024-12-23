'''2.	List sorting
sort the list of following names by –
1.	an ascending order of words 
2.	descending order of words 
3.	an ascending order of number of letters in each name 

unsortedList = ['Aaaa', 'bb', 'cccccccc', 'zzzzzzzzzzzz']
'''

unsortedList = ['Aaaa', 'bb', 'cccccccc', 'zzzzzzzzzzzz']
unsortedList.sort()
print("1.	an ascending order of words: ", unsortedList)

unsortedList.sort(reverse=True)
print("2.	descending order of words: ", unsortedList)

unsortedList.sort(key = len)
print("3.	an ascending order of number of letters in each name: ", unsortedList)
