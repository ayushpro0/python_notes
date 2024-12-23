'''2.	Given a string 
sentence = 'It is raining cats and dogs'
get 1 target list with length of each word in this sentence
Hint : Use map, lambda, split appropriately
'''

sen = 'It is raining cats and dogs'
result = list(map(lambda x: len(x), sen.split()))
print(result)