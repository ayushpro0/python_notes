# Variable number of Keyword arguments
# def dictVarArgs(arg1, arg2='defaultB', **theRest ,*x):  #Syntax Error
def dictVarArgs(arg1, arg2='defaultB', *x, **theRest):  # theRest ={c='grail',id='1000'}
    """arguments in dictionary In this **theRest is dictionary"""
    print('formal arg 1:', arg1)
    print('formal arg 2:', arg2)
    print("Tuple content = ", x)
    print("therest dict = ", theRest)
    k = theRest.keys()  # k is  a list ['id','c']
    k = list(k)
    print('keys = ', k)
    print('Var arg in dictionary = ', k[0], "Value = ", theRest[k[0]])
    print('Var arg in dictionary = ', k[1], "Value = ", theRest[k[1]])

    print("----------------------------------------------------")

    for eachXtrArg in theRest.keys():  # dictionary traversal     ['c','id']
        print('Xtra arg %s: %s' % (eachXtrArg, str(theRest[eachXtrArg])))


dictVarArgs(1220, 740.0, c='grail', id='1000')  # works

print("----------------------------------------------------")

# dictVarArgs(1220, 740.0, 100, 200)
# 100,200 are non keyword arg, so cannot be captured by **theRest variable

# dictVarArgs(1220, 740.0)              #works
dictVarArgs(1220, 740.0, 500, 600, c='grail', id='1000')  #

"""
kargs = {'one':1, 'two':2, 'three':3}
dictVarArgs(1220,740.0, **kargs)

"""
