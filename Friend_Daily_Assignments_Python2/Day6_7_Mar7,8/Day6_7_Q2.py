'''2.	Write a program to display all the prime numbers within an interval. Write a function for the same.'''
def check(st, ed):
    prime_li = [2]
    if st==1 or st == 2:
        st = 3
    for i in range(st, ed+1):
        for j in range(2, i//2+1):
            if i%j == 0:
                break
        else:
            prime_li.append(i)
    return prime_li

st = int(input("Enter starting number: "))
ed = int(input("Enter ending number: "))
li = check(st, ed)
print(li)


   