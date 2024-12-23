# STDIN, STDERR, STDOUT - default file handles

IN = open("data.txt", "r")  # IN is a file stream / object
# FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'

print("Functions of file Object: ", dir(IN))  # to show default attributes and methods of File Object

line1 = IN.readline()
print("line1 = ", line1)  # line1 =  Welcome to PSL!!!

line1 = IN.readline()
print("line1 = ", line1)  # line1 =  Learning Python !!!

IN.close()

# OUT = open ("data.txt", "w")
# OUT.writeline()

# example of dir()
list1 = [1, 2]
print(dir(list1))
