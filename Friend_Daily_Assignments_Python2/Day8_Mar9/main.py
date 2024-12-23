'''3.	Place implementation of above assignment 1  and 2 in a function inside a module file and then write final application with import to that module file and call the relevant functionalities from it.  '''

import country1

file1 = open("Country.txt", "r")
cnt = file1.readlines()

#print(cnt)
'''dic = {}

for i in cnt:
    lang, ctry = i.split(':')
    ctry = ctry.split()
    dic[lang] = ctry

print(dic)'''
dic = country1.getList(cnt)
print("list of languages with country: \n", dic)

print(country1.count_c(dic))
file1.close()
