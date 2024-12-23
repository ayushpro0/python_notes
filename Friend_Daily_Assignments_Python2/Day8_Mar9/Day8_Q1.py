'''1.	Count of languages
Store the Country data from country file only for Language and its count in a dictionary.
Display the o/p in below 2 formats –

>>> 
Portuguese 1
Franch 4
Chinese 1
Vietnamese 1
German 1
English 5
Japanese 1
Greek 1
Indian 1
Spanish 3
Arabic 2
Hungerian 1
Italian 1
--------------------------------------------------
{'Portuguese': 1, 'Franch': 4, 'Chinese': 1, 'Vietnamese': 1, 'German': 1, 'English': 5, 'Japanese': 1, 'Greek': 1, 'Indian': 1, 'Spanish': 3, 'Arabic': 2, 'Hungerian': 1, 'Italian': 1}

Q2.
{'Portuguese': ['Brazil'], 'Franch': ['Cameroon', 'Djibouti', 'Equatorial Guinea', 'France'], 'Chinese': ['China'], 'Vietnamese': ['Vietnam'], 'German': ['Germany'], 'English': ['United Kingdom', 'United States', 'Fiji', 'Canada', 'Ireland'], 'Japanese': ['Japan'], 'Greek': ['Greece'], 'Indian': ['India'], 'Spanish': ['Venezuela', 'Argentina', 'Honduras'], 'Arabic': ['Yemen', 'Bahrain'], 'Hungerian': ['Hungary'], 'Italian': ['Italy']}
'''

dic = {}
a = 'yes'

while(a == 'yes'):
    li = []
    cntry = input("Enter name of country:\n")
    b = 'yes'
    
    while(b == 'yes'):
        lang = input("Enter lang: \n")
        li.append(lang)
        b = input("want to add more languages? yes/no : \n")
    dic[cntry] = li
    a = input("Want to add country? yes/no \n")

print(dic) # output of question 2

dic_count = {}
for i in dic:
    dic_count[i] = len(dic[i])

print(dic_count) # output Q1
    

