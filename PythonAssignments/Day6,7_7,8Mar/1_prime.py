# 1.	Please enter a number and determine whether the number is prime or not.
# Write appropriate functions for the same.


def prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False

    return True


num = int(input("Enter the number: "))
if num <= 0:
    print("Invalid Input")

else:
    if (prime(num)):
        print(num, "is prime")
    else:
        print(num, "is not prime")
