# Keyboard Input Example


y = input("Enter your name : ")
# input function provides prompt to accept the user input from keyboard,input is  "" string
print("Type of y = ", type(y))
print("Hello", y)

"""
Output of input() function in Python3 as below->
Case1:
Enter your name : Sakshi
Type of y =  <class 'str'>
Hello Sakshi


Case2:
Enter your name : 100
Type of y =  <class 'str'>
Hello 100

Case 3:
Enter your name : 3+6
Type of y =  <class 'str'>
Hello 3+6

"""

"""
In Python 2.x, we had raw_input() function as shown below, not available in Python3
x = raw_input("Please enter ur name :")  #raw_input function provides prompt to accept the user input from keyboard, input is ""  string
print ("Type of x = ", type(x))
print ("Hello ", x) #"Sakshi"   ("10")
print ("-----------------------------------------------------")
"""

# Assignment
"""
Accept 2 numbers and print the addition
raw_input()

num1 = raw_input("Enter First Number")
num2 = raw_input("Enter Second Number")
answer = int(num1)+int(num2)
print "Addition of ", num1 , " and ", num2 , " = ", answer

"""
