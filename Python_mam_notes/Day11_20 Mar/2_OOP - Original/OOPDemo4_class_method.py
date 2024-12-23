class Circle:
    pi = 3.14159   #class variable
    all_circles=[]  #class variable  list
    def __init__(self, radius):
        self.radius = radius
        #self.pi =3.14
    def area(self):                                     #instance method
        return self.radius * self.radius * Circle.pi
    @classmethod
    def total_area(cls,o1):    #cls is catching argument as Classname  ---> Circle
        total = 0
        for c in cls.all_circles:
            total = total + c.area()
        return total
print ("---------------------------------------------------------------------")
print ("PI = ", Circle.pi)   #access class var
c1 = Circle(2)
print ("Area= ", c1.area())
c2 = Circle(3)
print ("Area= ", c2.area())
Circle.all_circles =[c1,c2]    #list of 2 Circle Objects
print ("Total area = ", Circle.total_area())   #when class method is called, Classname itself is passed as an implicit parameter





























































