'''1.	Accept a string, check whether it is palindrome
Eg. “madam”
'''

word = input("Enter a string: ")
if word == word[::-1]:
    print("It is palindrome.")
else:
    print("It is not a palindrome.")