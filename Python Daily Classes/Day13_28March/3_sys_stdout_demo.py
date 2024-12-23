import sys

sys.stdout = open("output_file.txt", "w") #redirecting console to file object

print("this is will be written in output_file.txt")

sys.stdout.close()


"""
OUT = open("target.txt", "w")
print("hello", file = OUT)
"""

"""
stdin
stdout
stderr

f1 = open("hello.txt", "w")
f1.write("hello!!!")
"""