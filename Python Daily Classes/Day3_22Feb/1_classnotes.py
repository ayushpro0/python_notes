s1 = "oooboo"
if s1 == s1[::-1]: # str == str True / False
        print("It is palindrome")
else:
        print("Not a palindrome")
# or

print("It is palindrome." if s1==s1[::-1] else "It is not palindrome.")

# -----------------------------------


s1 = "012345"
print("s1 = ", s1)

# s1[0] = "A" # TypeError: 'str' object does not support item assignment

s2 = """ a'b"d """

"""
comment block
"""

s3 = """Hello World!!
            Welcome to Python session!
                    Interesting!! """

print("s3 = ", s3)


