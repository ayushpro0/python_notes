# Problem
#
# Arun and Ravi are good friends. They are keen about programming, so their professor has given them a list and said them to come with a solution where the output should only return True if sublist of list will be present or else False. So, they want your help to make it complete. Kindly, help them to write a python program to check whether a list contains a sublist or not.
#
# Input Format :
#
# First line of input has to be given as a list with n number of integer elements.
#
# Second line of input should be the sublist that you want to check.
#
# Output Format :
#
# Output has to be only True of False. ( Refer sample input and output for formatting specifications )
#
# Sample Input1 :
#
# 2 4 3 5 7
#
# 4 3
#
# Sample Output1 :
#
# True
#
#
# Sample Input2 :
#
# 10 5 14 52 3 9 18 22 31 38 42 46 58 63 69 73 76 82 83 89 92 99 100
#
# 4 7 6 11
#
# Sample Output2 :
#
# False

list1 = list(map(str, input().split()))
list1s = ",".join(list1)

list2 = list(map(str, input().split()))
list2s = ",".join(list2)

if list2s in list1s:
    print("True")
else:
    print("False")