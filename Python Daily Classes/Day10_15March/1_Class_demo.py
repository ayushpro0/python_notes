class SayHello:  # class definition
    def __init__(self):  # constructor method
        print("Inside init constructor function...")
        print("self = ", self)  # <__main__.SayHello object at 0x00000231791BE290>

        # instance property
        self.message = "Hello World !!!"

    # instance method
    def display(self):
        print("self inside display = ", self)
        print("Message = ", self.message)


if __name__ == "__main__":
    ob1 = SayHello()
    # RHS => SayHello() loads a class memory, and
    # then passes the control to the default constructor # function,
    # __init__(self) by passing the memory ref as the default / implicit parameter

    print("Ob1 = ", ob1)  # Ob1 =  <__main__.SayHello object at 0x00000231791BE290> => default string representation

    # print("Ob1.message = ", ob1.message) # Hello World !!!

    ob1.display()  # passes the control to diplay() method, ob1 itself is passed as implicit parameter

    print("---------------------------------------")

    ob2 = SayHello()
    print("ob2 = ", ob2)
    # print("ob2 message = ", ob2.message)
    ob2.display()

    print("---------------------------------------")
