
myfile = open('data.txt', "r")
f = open("target.txt", "w") 
while True:
        str = myfile.readline()
        if str:
                print ("str = ", str)
                f.write(str)
        else:
                print ("Nothing in file")
                break
myfile.close()
f.close()

print ("myfile = ", myfile)      #O/P <closed file 'data.txt', mode 'r' at 0x0000000002E2E4B0>
print ("Current position = ", myfile.tell())   #ValueError: I/O operation on closed file










"""
fh = open ('country.txt', 'r')

country_lang ={}   #empty dictionary
for line in fh:

"""
