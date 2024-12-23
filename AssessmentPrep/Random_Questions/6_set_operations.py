s1 = set(input().split(","))
s2 = set(input().split(","))

c = int(input("choose one option 1) add 2)remove 3)difference 4)intersection"))
d = int(input("choose one 1)set1 2)set2"))

if d == 1:
    s = s1
elif d == 2:
    s = s2
else:
    print("invalid choice")
    exit()

if c == 1:  # add
    x = input()
    s.add(x)
    print("set(", sorted(s), ")")

elif c == 2:  # remove
    x = input()
    s.remove(x)
    print("set(", sorted(s), ")")

elif c == 3 and d == 1:  # difference set1 - set2
    print("set(", sorted(s1.difference(s2)), ")")

elif c == 3 and d == 2:
    print("set(", sorted(s2.difference(s1)), ")")

elif c == 4:
    print("set(", sorted(s1.intersection(s2)), ")")

else :
    print("invalid choice")



