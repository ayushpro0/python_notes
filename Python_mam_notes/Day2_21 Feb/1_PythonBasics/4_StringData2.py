# String Defination, raw string
s1 = "abc"
print("S1 = ", s1)

s2 = "That's"
print("s2 = ", s2)
# s2 = "That"s"#SyntaxError

s3 = """ a'b"c """
print("s3 = ", s3)  # a'b"c
# raw string
path1 = "c:\new\text.py"
print("path1 = ", path1)  # \n as newline , \t as tab got resolved

path1 = "c:\\new\\text.py"
print("path1 = ", path1)  # c:\new\text.py

path1 = r"c:\new\text.py"
print("path1 = ", path1)  # c:\new\text.py

path1 = R"c:\new\text.py"
print("path1 = ", path1)  # c:\new\text.py
