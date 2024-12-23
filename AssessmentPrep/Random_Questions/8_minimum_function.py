def findMinimun(*args):
    print(f"Minimum of {args} is {min(args)}")


print("Menu")
print("1. Minimum of 3")
print("2. Minimum of 4")
print("3. Minimum of 5")


choice = int(input())

if choice == 1:
    args = []
    for i in range(3):
        args.append(int(input()))

    findMinimun(*args)

elif choice == 2:
    args = []
    for i in range(4):
        args.append(int(input()))
    findMinimun(*args)

elif choice == 3:
    args = []
    for i in range(5):
        args.append(int(input()))
    findMinimun(*args)
else:
    print('invalid choice')


