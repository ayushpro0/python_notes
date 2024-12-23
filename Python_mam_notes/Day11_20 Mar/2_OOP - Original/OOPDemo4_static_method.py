class Circle:
    pi = 3.14159   #class variable
    def __init__(self, radius):             #constructor
        self.radius = radius

    def area(self):                         #instance method
        return self.radius * self.radius * Circle.pi
      
    @staticmethod
    def testing():
        print ("Inside testing method ....", Circle.pi)
        #print "Self radius = ", self.radius
        
    
print ("---------------------------------------------------------------------")
print ("PI = ", Circle.pi)   #access class var
c1 = Circle(2)
print ("Area= ", c1.area())     #instance method call
Circle.testing()                   #static method call over a class name







"""
@staticmethod
    def test():
        print "In testing.....",Circle.pi
        #print self.radius                      #NameError: global name 'self' is not defined
"""


