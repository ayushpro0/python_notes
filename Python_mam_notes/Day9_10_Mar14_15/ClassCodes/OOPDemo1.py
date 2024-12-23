
class SayHello:  # class defination
    def __init__(self):  # constructor method
        print("Inside init constructor function......")
        print ("Self= ", self)  # <__main__.SayHello object at 0x10325a5c0>
        self.message = "Hello World!!"  # instance property

    # instance method
    def display(self):
        print ("Self inside display = ", self)
        print("Messge = ", self.message)


if __name__ == "__main__":
    ob1 = SayHello()  # RHS SayHello() loads a class memory, and then passes the control to
    # the default constructor function ,__init__(self) by passing the memory ref as the default/implicit
    # parameter
    print("Ob1 = ", ob1)  # <__main__.SayHello object at 0x10325a5c0> default string representation
    # print("Ob1 message = ", ob1.message)
    ob1.display()  # passes the control tp display() method, ob1 itself is passed as implicit parameter
    print("-------------------------------------------")

    ob2 = SayHello()  # RHS SayHello() loads a class memory, and then passes the control to
    # the default constructor function ,__init__(self) by passing the memory ref as the default/implicit
    # parameter
    print("Ob2 = ", ob2)  # <__main__.SayHello object at 0x10325bc5> default string representation
    # print("Ob2 message = ", ob2.message)
    ob2.display()
    print("-------------------------------------------")

