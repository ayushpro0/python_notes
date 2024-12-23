'''1.	Please enter a number a number and determine whether the number is prime or not. Write appropriate functions for the same.'''

def checkPrime(num):
    for i in range(2,num//2+1):
        if num%i == 0:
            print("number is not prime")
            break
    else:
        print("Number is a prime number.")

num = int(input("Enter a number: \n"))
checkPrime(num)