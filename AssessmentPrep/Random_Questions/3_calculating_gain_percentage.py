a = int(input("Enter the price of the old scooter: \n"))
b = int(input("Enter the amount spent on repairs: \n"))

sell_price = float(input("Enter the selling price: \n"))

cost_price = a + b

profit = sell_price - cost_price

gain_percent = (profit/cost_price)*100

print("The gain percentage is %.2f" %gain_percent)