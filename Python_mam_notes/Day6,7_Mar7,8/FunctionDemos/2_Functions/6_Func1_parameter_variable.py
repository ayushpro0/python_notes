# Variable number of Positional arguments (non-keyword arguments)
# def tupleVarArgs(*theRest, arg1, arg2='defausltB'):   #Syntax Error
def tupleVarArgs(arg1, arg2='defaultB', *theRest):
    # *theRest is tuple can consume only non-keyword argument  ('xyz', 456.789)

    """variable arguments"""
    print('formal arg 1:', arg1)
    print('formal arg 2:', arg2)
    print("theRest tuple = ", theRest)  # whole tuple is printed   ('xyz', 456.789)
    for eachXtrArg in theRest:
        print('another arg:', eachXtrArg)


# calling functions
tupleVarArgs('abc', 123, 'xyz', 456.789)  # this works   non-keyword arguments passed
# theRest = ('xyz', 456.789)

print("----------------------------------------------------")

tupleVarArgs('abc', 123, [1, 2, 3], ['A', 'b'])  # works

print("----------------------------------------------------")

tupleVarArgs('abc', 123, arg4='xyz')
# run time Typeerror    arg4 = 'xyz'--->keyword argument

print("----------------------------------------------------")

tupleVarArgs('abc')  # this works *theRest tuple willbe empty

"""
print "----------------------------------------------------"

tupleVarArgs('abc', 123, 'xyz')
t1 = (1,)
print "t1 =", t1

l1 =[10]
print "l1 = ",l1[0]
"""
