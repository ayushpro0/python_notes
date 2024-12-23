# 2.	Write a program to display all the prime numbers within an interval. Write a function for the same.

def prime(num):
    if num == 1 or num == 0:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False

    return True


def primeRange(start, end):
    for i in range(start, end + 1):
        if prime(i):
            print(i, end=" ")


start = int(input("start: "))
end = int(input("end : "))

if start >= 0 and end > 1:

    primeRange(start, end)

else:
    print("invalid range")
