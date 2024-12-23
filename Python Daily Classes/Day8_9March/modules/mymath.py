# module file defination
# mymath - our example math module

pi = 3.14159

def area(r): # area(r) => returns the area of a circle with radius r
    global pi
    return (pi * r * r)

# write Fibonacci series up to n
def fib(n):
    a, b = 0, 1
    while b < n:
        print (b)
        a, b = b, a+b # tuple
# print("=====================================================") # cannot have executable lines in a module

if __name__ == "__main__" : 
    print("=====================================================") 
    fib(21)
    print(area(5))

    print('======================================================')
