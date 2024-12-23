# sys.path
# command line arguments

import sys

# print("argv list = ", sys.argv) # show the current path of the file, if no arguments are given

if (len(sys.argv) == 2) :
    print("argv list = ", sys.argv) # ['.\\2_sys_command_line_arg_demo.py', '20']
    print("First argument from argv list = ", sys.argv[0]) #current file name => .\2_sys_command_line_arg_demo.py
    print("Second argument from argv list = ", sys.argv[1]) #20
    print("---------------------------------------------------")
    print(dir(sys))

else :
    print("Insufficient arguments!!! try again!!!")

print("--------------------------------------------------------")

s = "Persistent!!!"
print("s = ", s)
# print("string object details = \n", dir(s))


















# python .\2_sys_command_line_arg_demo.py 10 20
# argv list =  ['.\\2_sys_command_line_arg_demo.py', '10', '20']