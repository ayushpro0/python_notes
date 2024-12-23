brand_exp = int(input("Enter the branding expenses: "))
travel_exp = int(input("Enter the travel expenses: "))
food_exp = int(input("Enter the food expenses: "))
logistics_exp = int(input("Enter the logistics expenses: "))

total_exp = float(brand_exp + travel_exp + food_exp + logistics_exp)
print("Total expenses : Rs.%.2f" %total_exp)

brand_percent = (brand_exp / total_exp) * 100
print("Branding expenses percentage : ", "%.2f" %brand_percent, "%")

travel_percent = (travel_exp / total_exp) * 100
print("Travel expenses percentage : ", "%.2f" %brand_percent, "%")

food_percent = (food_exp / total_exp) * 100
print("Food expenses percentage : ", "%.2f" %food_percent, "%")

logistics_percent = (logistics_exp / total_exp) * 100
print("Logistics expenses percentage : ", "%.2f" %logistics_percent, "%")
