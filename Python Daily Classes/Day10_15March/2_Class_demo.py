class SayHello:  # class definition

    count = 0  # class level variable

    def __init__(self, msg="Hello World!!!"):  # constructor method -parameterized -overloading
        # instance property
        self.message = msg
        SayHello.count += 1

    # instance method
    def display(self):
        print("Message = ", self.message)

    @staticmethod  # decorator
    def getCount():
        print("Count = ", SayHello.count)

    @classmethod  # class method
    def getCount2(cls):
        print("cls = ", cls)  # cls =  <class '__main__.SayHello'>
        print("count in classmethod = ", cls.count)


if __name__ == "__main__":
    # ob1 = SayHello("Welcome to PSL!!!")
    ob1 = SayHello()

    # print("Ob1.message = ", ob1.message) # Hello World !!!

    ob1.display()  # passes the control to diplay() method, ob1 itself is passed as implicit parameter

    print("---------------------------------------")

    # ob2 = SayHello("Learning Python!!!")
    ob2 = SayHello("Welcome to PSL!!!")

    # print("ob2 message = ", ob2.message)

    ob2.display()

    print("---------------------------------------")

    # print("Count = ", SayHello.count) # Count = 2
    SayHello.getCount()  # Nothing is passed as implicit parameter
    SayHello.getCount2()  # SayHello.getCount2() takes 0 positional arguments but 1 was given
    # SayHello class name itself is passed as implicit parameter
