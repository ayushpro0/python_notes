# 1.	Accept a string, check whether it is palindrome
# E.g. “madam”


string = input("Enter the string \n")

if string == string[::-1]:
    print(string, "is Palindrome")
else:
    print(string, "is not a Palindrome")
