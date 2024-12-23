class SayHello:  # class defination
    count = 0  # class level variable

    def __init__(self, msg="Hello World!!"):  # constructor method - parameters - overloading
        print("Inside init constructor function......")
        print("Self= ", self)  # <__main__.SayHello object at 0x10325a5c0>
        self.message = msg
        SayHello.count += 1

    def display(self):  # #instance method
        print("Self inside display = ", self)
        print("Messge = ", self.message)

    @staticmethod
    def getCount():
        print("Count = ", SayHello.count)

    @classmethod
    def getCount2(cls):
        print("cls = ", cls)  # <class '__main__.SayHello'>
        print("Count in classmethod = ", cls.count)


if __name__ == "__main__":
    ob1 = SayHello()  # RHS SayHello() loads a class memory, and then passes the control to
    # the default constructor function ,__init__(self) by passing the memory ref as the default/implicit
    # parameter
    print("Ob1 = ", ob1)  # <__main__.SayHello object at 0x10325a5c0> default string representation
    # print("Ob1 message = ", ob1.message)
    ob1.display()  # passes the control tp display() method, ob1 itself is passed as implicit parameter
    print("-------------------------------------------")

    ob2 = SayHello("Welcome to PSL!!")  # RHS SayHello() loads a class memory, and then passes the control to
    # the default constructor function ,__init__(self) by passing the memory ref as the default/implicit
    # parameter
    print("Ob2 = ", ob2)  # <__main__.SayHello object at 0x10325bc5> default string representation
    # print("Ob2 message = ", ob2.message)
    ob2.display()
    print("-------------------------------------------")
    # print("Count = ", SayHello.count)
    SayHello.getCount()  # Nothing is passed as implicit parameter
    SayHello.getCount2()  # TypeError: SayHello.getCount2() takes 0 positional arguments but 1 was given
    # SayHello class name itself is passed as implicit parameter
