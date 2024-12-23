# parent class
class Parent:
    """Parent class"""

    def __init__(self):
        print('Parent created an instance of', self.__class__.__name__)

    def greet(self):  # instance method
        print('Hi, I am Parent-greet()')


# child class
class Child(Parent):
    def __init__(self):
        print('Child created an instance of', self.__class__.__name__)

    def greet(self):  # over ridding method
        print('Hi, I am Child-greet()')
        # Parent.greet(self)


# --------------------------------------------------------------------------

c = Child()  # c is an instance of subclass Child
c.greet()  # c itself was passed as an implicit parameter

print("------------------------------------------")

# Parent.greet()#TypeError: Parent.greet() missing 1 required positional argument: 'self'
Parent.greet(c)  # runtime polymorphism

# subclass  call a base
# class method which is
# overridden in the subclass
# Parent.greet()   #run time error as TypeError unbound
# Break time till 4.30
