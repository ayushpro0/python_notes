# String definition, raw string

s1 = "abc"
print("s1 = ", s1)

s2 = "That's"
print("s2 = ", s2)

# s2 = "That"s" #SyntaxError

s3 = """ a'b"c """
print("s3 = ", s3)  # a'b"c

# Raw String
path1 = "c:\new\text.py"

print("path1 = ", path1)  # \n as newline, \t as tab got resolved
# output -> path1 = c:
#           ew      ext.py

path1 = "c:\\new\\text.py"
print("path1 = ", path1)  # escape OUTPUT: path1 =  c:\new\text.py

path1 = r"c:\new\text.py"
print("path1 = ", path1)  # using raw string
# OUTPUT -> path1 =  c:\new\text.py

path1 = R"c:\new\text.py"  # doesn't matter if its r or R
print("path1 = ", path1)
