class oPair:  # ordered pair
    def __init__(self, obj1, obj2):  # constructor
        self.data = (obj1, obj2)  # assign attribute

    def __str__(self):  # str() string representation
        return str(self.data)  # convert tuple to string

    __repr__ = __str__  # repr() string representation

    def __add__(self, other):  # add two oPair objects
        return self.__class__(self.data[0] + other.data[0], self.data[1] + other.data[1])
        # oPair class constructor is called   oPair(1,5)
        # self.__class__(1,5)
        # oPair(1,5)


# -------------------------------------------------
print(dir(object))

myPair = oPair(6, -4)  # create instance
print("myPair = ", myPair)  # calls myPair.__str__()

pair1 = oPair(6, -4)
pair2 = oPair(-5, 9)
print("Pair 1= ", pair1)
print("Pair 2= ", pair2)

print("Addition = ", pair1 + pair2)  # pair1.__add__(pair2)   2 parameters are passed
# TypeError: unsupported operand type(s) for +: 'oPair' and 'oPair' if add method not implemented

print("------------------------------------------------")

# print dir(oPair)

# print dir(object)
# int+int   float+float  int+float   newstr = str1 +str2   newlist = list1+list2
# all these object have the implementation of __add__() method
# int + str   TypeError


"""
def __add__(self, other):       # add two oPair objects
        return self.__class__(self.data[0] + other.data[0],self.data[1] + other.data[1])
    
"""
