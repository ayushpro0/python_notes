import random
my_list =[100,1,99,44,22,66]
print ("Original list =",my_list)  #Original list = [100, 1, 99, 44, 22, 66]

random.shuffle(my_list) 

print ("Random list =",my_list)    #Random list = [44, 22, 100, 1, 66, 99]
print ("---------------------------------------------------------------------")
print ("random choice from a list= ",random.choice(['apple', 'pear', 'banana']) )  #pear
print ("---------------------------------------------------------------------")
print ("Random float number = ",random.random() )     # Random float number =  0.565145164752
print ("---------------------------------------------------------------------")

print (random.randrange(4) )  #random.randrange(4)     #[0,1,2,3]
