

import sys
sys.stdout = open("hello.txt","w") #redirecting console to file object
print "AAAAAAAAAAAAAAAAaa"  #instead of printing on console, it will print inside file hello.txt 
sys.stdout.close()





'''
stdin
stdout
stderr


 f1 = open("hello.txt","w")
 f1.write("Hello !!!")
'''
