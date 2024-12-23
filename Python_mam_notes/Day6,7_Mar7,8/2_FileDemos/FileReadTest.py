
# STDIN, STDERR, STDOUT - default file handles

IN = open("target.txt", "r")  # IN is a file stream/object
# FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'


print("Functions of File Object = ", dir(IN))  # returns a list of all methods of File Object

line1 = IN.readline()  # EOL
print("line1 = ", line1)

line1 = IN.readline()
print("line1 = ", line1)


IN.close()

"""
OUT = open ("data.txt", "w")
OUT.writeline()


list1 =[1,2]
dir(list1)
"""
