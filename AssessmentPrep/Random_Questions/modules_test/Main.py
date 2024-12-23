from package_example import *


while True:
    choice = int(input("1.addition Modulo\n2.Sum of odd and even\n3.jubliee or not\n"))

    if choice == 1:
        n = int(input())
        x = int(input())
        m = int(input())
        print(addition_modulo(n, x, m))

    elif choice == 2:
        n = int(input())
        odd_sum, even_sum = even_odd_sum(n)
        print(odd_sum, even_sum)
    elif choice == 3:
        n = int(input())
        print(is_jubliee(n))
    else:
        print("invalid choice")

    cont = input("Do you want to continue?(y/n)")
    if cont.lower() != 'y':
        break