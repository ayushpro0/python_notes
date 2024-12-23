#List data tuple data Example
listOne= [123, 'abc', 4.56]                 #List defination with different data objects, List is mutable
print "listOne = ",listOne                  #listOne =  [123, 'abc', 4.56]
#Tuple --->immutable
tupleOne= (123, 'abc', 4.56)                #Tuple defination with different data objects, Tuple is immutable
print "tupleOne = ",tupleOne                #tupleOne =  (123, 'abc', 4.56)
print "-------------------------------------------------------------------"
print "First element of listOne = ", listOne[0]     #First element of listOne =  123
print "First element of tupleOne = ", tupleOne[0]   #First element of tupleOne =  123
print "slicing of listOne from index 0 upto 2 = ",listOne[0:2]  #slicing of listOne from index 0 upto 2 =  [123, 'abc']
print "-------------------------------------------------------------------"

            #inner list
listTwo= [4.56, ['inner', 'list']]          #inner list defined
print "Inner listTwo = ",listTwo            #Inner listTwo =  [4.56, ['inner', 'list']]
            #inner Tuple
tupleTwo = (123, 'abc', 4.56, ['inner', 'tuple'], 7-9j)
print "Tuple with inner List = ",tupleTwo   #Tuple with inner List =  (123, 'abc', 4.56, ['inner', 'tuple'], (7-9j))
t2 =(10,20,(1,2,3))
print "Tuple with inner tuple = ", t2       #Tuple with inner tuple =  (10, 20, (1, 2, 3))
print "-------------------------------------------------------------------"

listFour= [123, 'abc', 4.56, ['inner', 'list']]
print "List listFour = ", listFour
print "3rd index element of istFour = ", listFour [3]   #3rd index element of istFour =  ['inner', 'list']
#print "6th index inner list = ", listFour [6] #run time error IndexError: list index out of range
print "first index element of inner list from listFour= " , listFour [3][1] #first index element of inner list from listFour=  list
print "-------------------------------------------------------------------"
a=12,34,5 #comma seperated objects without any bractes defaults to tuple defination
print "Tuple a = ",a
print "-------------------------------------------------------------------"













































