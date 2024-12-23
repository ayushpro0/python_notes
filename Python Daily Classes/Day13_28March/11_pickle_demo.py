import pickle #shelve

d = {'foo' : 'bar', 'cat' : 'tar'} #dictionary

FH = open('foo.txt', 'bw') #FW.write("")
pickle.dump(d, FH) # save dictionary object d (in pickle string format) in file foo.txt

L = ['hi', 'world']
pickle.dump(L, FH)

s = 'bye world'
pickle.dump(s, FH)

FH.close()

print("-----------------------------------------------------------")

FH = open('foo.txt', 'br')
d1 = pickle.load(FH) # unpickling by load function, givees me dictionary back by reading it
print(d1)
print("foo value = ", d1['cat'])

l2 = pickle.load(FH) # gives me lsit
print(l2)

s2 = pickle.load(FH) # gives me string
print(s2)