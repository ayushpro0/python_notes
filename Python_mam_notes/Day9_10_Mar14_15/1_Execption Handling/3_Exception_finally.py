try:
    testfile = open('data.txt')
    try:
        txns = testfile.readlines()
        print ("File data = ",txns)
    finally:
        print ("In Inner finally")
        
except IOError:
    print ('unable to access test file\n')
   
finally:
        print ("In Outer finally")
        
        #testfile.close()


print ("In END!!!!")

"""
1)
open('data11111.txt')
this file does not exists

>>> 
unable to access test file

In Outer finally
In END!!!!



2)
testfile = open('data.txt')
>>> 
File data =  ['PSL\n', 'Welcome to PSL\n', 'Pune\n', '2015 BYE!!!!']
In Inner finally
In Outer finally
In END!!!!


3)
testfile = open('data.txt')
    try:
        txns = testfile.readlines()
        print "File data = ",tx

NameError

        
"""


 
"""
if testfile <> None 
testfile.close()
"""
