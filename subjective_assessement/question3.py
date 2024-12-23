# Customer - ItemRating - Item
# [Note :
# Strictly adhere to the object-oriented specifications given as a part of the problem statement.
# Use the same class names and member variable names. ]
#
# Write a program to find
#
# the favorite Items(rating > 3) of a particular user and
# the customers who hated a particular item
# Create a class Customer with the following datamembers.
#
# Data Type	Variable Name
# Integer	customerId
# String	customerName
# String	customerContactNumber
# String	email
#
# Include a 4-argument constructor. The order of parameters passed to the constructor is customerId,customerName,customerContactNumber,email
#
#
#
# Create a class Item with the following data members.
#
# Data Type	Variable Name
# Integer	itemId
# String	name
# String	description
# String	price
#
# Include a 4-argument constructor. The order of parameters passed to the constructor is itemId, name, description, price
#
#
# Create a class Rating with the following data members.
#
# Data Type	Variable Name
# Customer	customerObject
# Item	itemObject
# String	review
# Integer	ratingstar
# Include a 4-argument constructor. The order of parameters passed to the constructor is customerObject,itemObject,review,ratingstar
#
# Note:
#
#
# For Example
# we give three Rating Inputs
#
# Customer Id	Item Id	Review	Rating star
# 1	1	good	4
# 2	2	excellent	5
# 2	1	too dry	2
#
# If customer id is 1:
# his favorite items are
#
# Item 1
# Then, if the item id is 1:
# the customers who hated the item are
#
# Customer 2
#
# Sample Input and Output :
#
#
# Enter the Number of Customers
# 2
# Enter the Customer id
# 1
# Enter the Customer name
# JK
# Enter the Contact Number
# 23105
# Enter the email
# jk@a.com
# Enter the Customer id
# 2
# Enter the Customer name
# peri
# Enter the Contact Number
# 123231
# Enter the email
# per@a.com
# Enter the Number of Items
# 2
# Enter the Item id
# 1
# Enter the  Item name
# Chapathi
# Enter the Description
# made of Wheat flour
# Enter the Price
# 22.5
# Enter the Item id
# 2
# Enter the  Item name
# Idli
# Enter the Description
# made of rice flour
# Enter the Price
# 15
# Enter the No of Ratings received
# 3
# Enter the Customer Id
# 1
# Enter the Item id
# 1
# Enter the Review
# good
# Enter the No of Rating stars for this item
# 4
# Enter the Customer Id
# 2
# Enter the Item id
# 2
# Enter the Review
# excellent
# Enter the No of Rating stars for this item
# 5
# Enter the Customer Id
# 2
# Enter the Item id
# 1
# Enter the Review
# too dry
# Enter the No of Rating stars for this item
# 2
# Enter the Customer Name
# JK
# Favorite Items of JK are:
# Item Id: 1
# Item Name: Chapathi
# Description: made of Wheat flour
# Price: 22.5
# Enter the Item Name
# Chapathi
# Customers who hate Chapathi are:
# Customer Id: 2
# Customer Name: peri
# Contact Number: 123231
# Email: per@a.com




from Customer import Customer
from Item import Item
from Rating import Rating
#fill your code here

customer_list = []

n_customer = int(input("Enter the Number of Customers\n"))

for i in range(n_customer):

    c_id = input("Enter the Customer id\n")
    c_name = input("Enter the Customer name\n")
    c_number = input("Enter the Contact Number\n")
    c_email = input("Enter the email\n")

    customer = Customer(c_id, c_name, c_number, c_email)
    customer_list.append(customer)

n_item = int(input("Enter the Number of Items\n"))
item_list = []

for i in range(n_item):

    i_id = input("Enter the Item id\n")
    i_name = input("Enter the Item name\n")
    i_desc = input("Enter the Description\n")
    i_price = input("Enter the Price\n")

    item = Item(i_id, i_name, i_desc, i_price)
    item_list.append(item)

n_rating = int(input("Enter the No of Ratings received\n"))
rating_list = []

for i in range(n_rating):
    c_id = input("Enter the Customer Id\n")
    i_id = input("Enter the Item id\n")
    review = input("Enter the Review\n")
    rating = input("Enter the No of Rating stars for this item\n")

    rating = Rating(c_id, i_id, review, rating)
    rating_list.append(rating)


cust_name = input("Enter the Customer Name\n")
print("Favorite Items of", cust_name, "are:")

customer_id = 0
for cust in customer_list:
    if cust.customerName == cust_name:
        customer_id = cust.customerId

customer_rating_list = []
item_bought_customer = []

for rating in rating_list:
    if rating.customerObject == customer_id:
        id = rating.itemObject
        rate = int(rating.ratingstar)
        customer_rating_list.append([id, rate])

if customer_rating_list:
    customer_rating_list.sort(key = lambda x: x[1], reverse = True)

# favourite = customer_rating_list[0]
for fav in customer_rating_list:
    if fav[1] > 3:
        for item in item_list:
            if item.itemId == fav[0]:
                print("Item Id:", item.itemId)
                print("Item Name: ", item.name)
                print("Description:", item.description)
                print("Price:", item.price)

hate_item = input("Enter the Item Name\n")
print("Customers who hate", hate_item,"are:")

hate_item_id = 0
for item in item_list:
    if item.name == hate_item:
        hate_item_id = item.itemId

item_review_list = []

for rate in rating_list:
    if rate.itemObject == hate_item_id:
        id = rate.customerObject
        review = int(rate.ratingstar)
        item_review_list.append([id, review])


if item_review_list:
    item_review_list.sort(key = lambda x: x[1])

hater = item_review_list[0]

for cust in customer_list:
    if cust.customerId == hater[0]:
        print("Customer Id:", cust.customerId)
        print("Customer Name:", cust.customerName)
        print("Contact Number:", cust.customerContactNumber)
        print("Email:", cust.email)





