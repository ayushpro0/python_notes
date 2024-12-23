import sys
import os
if(os.path.exists("myfile1.txt")):
        sys.stderr.write("File already exists")
        sys.exit(1)

f=open("myfile.txt","w")
f.write("Hello World\n")
f.close()
f =open("myfile.txt","r")
while True:
        x = f.readline()
        if x:
                print x
        else:
                break


print "------------------------------------------------------"
print os.listdir('.')
#os.chdir('/')
#os.mkdir("path")
print  "---------------------------------------------"
print "Os facilities = ", dir(os)


