# write to file
# f = open("c:\\data\\myfile.txt", "w")  # file  object created in write mode

f = open("myfile.txt", "w")  # file  object created in write mode, in current folder
print(dir(f))

print("-------------------------------------------------------------------")
f.write("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ\n")
f.write("BBBBBBBBBBBBBBAAAAA\n")
f.write("END!!")
f.close()

"""
print "----------------------------------------------------------------------------------"
str = "Hello"
print dir (str)
print "----------------------------------------------------------------------------------"
l1  =[1,2,3,4,5]
print "Functionalities for a list = ", dir(l1)
"""

"""

print "-------------------------------------------------------------------"
str = "Hello"
print dir(str)
print "-------------------------------------------------------------------"
l1=[1,2,3]
print dir(l1)
print "-------------------------------------------------------------------"
"""
