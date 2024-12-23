# try-except statement
def reading():
    # f = open('data11111.txt')     #default read mode       IOError:
    try:
        f = open('data111.txt')  # default read mode
    except IOError as a:
        print('could not open file =', a)  # exception handler code


print("Learning Exception Handling......")
reading()  # calling a function
print("END!!!!!")

"""
try:
        f = open('data.txt')     #default read mode
    except IOError as a:
        print 'could not open file =', a    #exception handler code
"""
