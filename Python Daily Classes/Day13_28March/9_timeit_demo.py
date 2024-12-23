from timeit import Timer # timeit is a module file, Timer class in this file

t1 = Timer('t = a; a = b; b = t', 'a = 1; b = 2').timeit() #instance method
print("t1 = ", t1)

t2 = Timer('a,b = b,a', 'a = 1; b = 2').timeit()
print("t2 = ", t2)

# t1 =  0.029845700002624653
# t2 =  0.024047999999311287 t2 is faster