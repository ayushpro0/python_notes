# Q2. 16 June

# Input :-
# 5
#
# Xyz : 340
# Wheat : 500
# Rice : 650
# Sugar : 250
# Dal : 400
#
# 3
#
# Output :-
#
# {'Rice':650.00, 'Wheat':500.00, 'Dal':400.00, 'Xyz':340.00, 'Sugar':250.00}
#
# Rice 650.00
# Wheat 500.00
# Dal 400.00

# -----------------------------------------------------------------

# Read the number of items
num_items = int(input())

# Create an empty dictionary to store the items and their prices
items_dict = {}

# Read the items and their prices
for _ in range(num_items):
    item, price = input().split(':')
    items_dict[item.strip()] = format(float(price), ".2f")  # format(inputNumber,".2f")

# Sort the items dictionary in descending order by their prices
sorted_items = dict(sorted(items_dict.items(), key=lambda x: float(x[1]), reverse=True))

# Print the sorted dictionary
print(sorted_items)

# Print the top 3 items
output_count = int(input())
count = 0

for item, price in sorted_items.items():
    print(f"{item}: {price}")
    count += 1
    if count == output_count:
        break
