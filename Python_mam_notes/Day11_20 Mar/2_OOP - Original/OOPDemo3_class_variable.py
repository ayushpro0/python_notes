class Circle:
    pi = 3.14159                    #class variable
    count =0
    def __init__(self, radius=1):     #constructior with 2 parameters  (instance, radius)
        self.radius = radius
        Circle.count +=1

    def area(self):                 #instance method
        return self.radius * self.radius * Circle.pi
print ("---------------------------------------------------------------------")
if __name__=="__main__":
    print ("PI = ", Circle.pi)   #access class var
    c1 = Circle(2)             #here defualt constructor __init__(self,2) gets called
    print ("Area= ", c1.area())   #insatnce method call, c1 itself is passed as an argument
    print ("PI = ", c1.pi)   #access class var
    c2 = Circle(5)
    print ("Area= ", c2.area())
    print ("Total number of Circle Objects = ", Circle.count)
