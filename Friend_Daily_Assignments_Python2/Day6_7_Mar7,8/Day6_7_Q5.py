'''5.	Write a Python program (function) to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
Consider the sample strings in a list as- (['abc', 'xyz', 'aba', '1221']
'''
li = ['abc', 'xyz', 'aba', '1221', 'eye']
c = 0
for i in li:
    if len(i)>=2 and i[0]==i[-1]:
        c+=1
print(c)