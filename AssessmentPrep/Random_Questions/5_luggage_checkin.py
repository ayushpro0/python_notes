weight = int(input("Enter the weight of luggage: "))

if weight <= 0:
    print("invalid input")
    exit()

if weight <= 15:
    print("No need to pay extra amount")

W = weight - 15

if W > 0 and W <= 30:
    pay = W*50
    print("Need to pay extra amount of Rs.%d" %pay)

elif W > 30 and W <= 60:
    pay = W*150
    print("Need to pay extra amount of Rs.%d" %pay)
else:
    pay = W * 250
    print("Need to pay extra amount of Rs.%d" %pay)
