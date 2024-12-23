import pickle  #shelve
d = {'foo':'bar','cat':'tar'}    #dictionary
FH =open('foo.txt','bw')
pickle.dump(d,FH)   #save dictionary object d (in pickle string format )in file foo.txt   writting

L=['hi','world']            #list
pickle.dump(L,FH)
s='bye world'               #string
pickle.dump(s,FH)
FH.close
#-----------------------------------------------------------------------------



FH=open('foo.txt','br')
d1 = pickle.load(FH)   #unpickling by load function, gives me dictionary back by reading it
print (d1)
print ("foo value =", d1['cat'])

d2 = pickle.load(FH)    #gives me list 
print (d2)

d2 = pickle.load(FH)    # #gives me string
print (d2)


'''
This is an amazing module that can take almost any Python object (even some
forms of Python code!), and convert it to a string representation;
this process is called pickling.
Reconstructing the object from the string representation is called unpickling.
Between pickling and unpickling, the string representing the object may have
been stored in a file or data, or sent over a network connection to some
distant machine.

pickle is the standard way to make Python objects which can be stored and
reused by other programs or by a future invocation of the same program;
the technical term for this is a persistent object.

'''








