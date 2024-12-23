
#command line argumnets
import sys
if (len(sys.argv)==2):
    print "argv list = ",sys.argv   #is a list
    print "First argumnet fron argv list = ",sys.argv[0]  #current file name
    print "Second argument from argv list =",sys.argv[1]
    print "-----------------------------------------------------------"
    print dir(sys)
else:
    print "Insufficient arguments!!!try again!!!"
print "-----------------------------------------------------------"
s= "Persistent!!!!"
print "s = ",s
print "string object details = \n", dir(s)
