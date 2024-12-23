'''Sample Input :
Enter the number OrderDetails to be added
1
Enter the details of Order 1
Enter the first name
deva
Enter the last name
muthu
Enter the date of birth(dd-mm-yyyy)
11-11-1998
Enter the age
21
Enter the street
rk
Enter the city
cbe
Enter the Pincode
441526
Enter the Product Name
mouse
Enter the Product Brand
lg
Enter the Product Type
mouse
Enter the Product Color
black
Enter the Customer Name
kumar
Enter the Ordered Date
16-03-2019
Enter the Delivery Date
18-03-2019
Enter the Customer name whose details need to be displayed
kumar
Sample Output :
Order Details
Customer Name : deva
Ordered Date : muthu
Delivery Date : 21
Product Details
Product Name : mouse
Product Brand : lg
Product Type : mouse
Product Color : black
User Details
First Name : deva
Last Name : muthu
DOB : 11-11-1998
Age : 21
Addres of the Order
Street : rk
City : cbe
PIN code : 441526
'''
class User:

    # fill your code
    def __init__(self, Fname, Lname, dob, age):
        self.Fname  = Fname
        self.Lname = Lname
        self.dob = dob
        self.age = age

    def displayUserDetails(self):
        # fill your code
        print("User Details")
        print("First Name : {}\nLast Name : {}\nDOB : {}\nAge : {}".format(self.Fname, self.Lname, self.dob,self.age))

class Address:

    # fill your code
    def __init__(self, street, city, pin):
        self.street = street
        self.city = city
        self.pin = pin

    def displayAddressDetails(self):
        # fill your code
        print("Addres of the Order")
        print("Street : {}\nCity : {}\nPIN code : {}\n".format(self.street, self.city, self.pin))


class Product:

    # fill your code
    def __init__(self, Pname,Pbrand,Ptype,Pcolor):
        self.Pname = Pname
        self.Pbrand = Pbrand
        self.Ptype = Ptype
        self.Pcolor = Pcolor

    def displayProductDetails(self):
        # fill your code
        print("Product Details")
        print("Product Name : {}\nProduct Brand : {}\nProduct Type : {}\nProduct Color : {}\n".format(self.Pname, self.Pbrand, self.Ptype, self.Pcolor))


class RentalOrderDetails(User , Address , Product):

    # fill your code

    def __init__(self, uobj, aobj, pobj,cus_name,ord_date, del_date):
        self.uobj = uobj
        self.aobj = aobj
        self.pobj = pobj

        self.cus_name = cus_name
        self.ord_date = ord_date
        self.del_date = del_date

    @classmethod
    def displayOrderDetails(self , li , cus_name):
        # fill your code
        for i in li:
            if i.cus_name == cus_name:
                print("Order Details\nCustomer Name : {}\nOrdered Date : {}\nDelivery Date : {}\n".format(i.cus_name, i.ord_date, i.del_date))
                i.pobj.displayProductDetails()
                i.uobj.displayUserDetails()
                i.aobj.displayAddressDetails()



# Main
n = int(input("Enter the number OrderDetails to be added\n"))
c = 1
li = []
for i in range(n):
    print("Enter the details of Order %d"%c)
    fname = input("Enter the first name\n")
    lname = input("Enter the last name\n")
    dob = input("Enter the date of birth(dd-mm-yyyy)\n")
    age = input("Enter the age\n")
    street = input("Enter the street\n")
    city = input("Enter the city\n")
    pin = input("Enter the Pincode\n")
    pname = input("Enter the Product Name\n")
    pbrand = input("Enter the Product Brand\n")
    ptype = input("Enter the Product Type\n")
    pcolor = input("Enter the Product Color\n")
    cname = input("Enter the Customer Name\n")
    odate = input("Enter the Ordered Date\n")
    ddate = input("Enter the Delivery Date\n")
    # fill your code
    uobj = User(fname, lname, dob, age)
    aobj = Address(street, city, pin)
    pobj = Product(pname, pbrand, ptype, pcolor)
    obj = RentalOrderDetails(uobj,aobj,pobj,cname, odate, ddate)
    li.append(obj)

cname = input("Enter the Customer name whose details need to be displayed\n")
RentalOrderDetails.displayOrderDetails(li, cname)


