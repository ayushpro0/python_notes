class Circle:
    pi = 3.14159   #class variable
    all_circles=[]
    def __init__(self, radius=None):    #radius=None   it is a default parameter
        if(radius is None):
            self.radius =2
        else:
            self.radius = radius

    def area(self,*theRest):
        print ("In area , tuple var = ",theRest)
        #Circle c1 = theRest[0]
        #Circle c2 = theRest[1]
        #print ("C1 Object = ",theRest[0])
        
        return self.radius * self.radius * Circle.pi

    @classmethod
    def total_area(cls):
        total = 0
        for c in cls.all_circles:
            total = total + c.area()
        return total
print ("---------------------------------------------------------------------")
print ("PI = ", Circle.pi)   #access class var
c1 = Circle()
print ("Area= ", c1.area())
print ("---------------------------------------------------------------------")
c2 = Circle(3)
print ("Area= ", c2.area())
print ("---------------------------------------------------------------------")
Circle.all_circles =[c1,c2]
print ("Total area = ", Circle.total_area())
c2.area(Circle.all_circles)

"""
class Cheese():
    def __init__(self, num_holes = None):
        if(num_holes is None):
            ...

Now if you want complete freedom of adding more parameters:
class Cheese():
    def __init__(self, *args, **kwargs):
        #args -- tuple of anonymous arguments
        #kwargs -- dictionary of named arguments
        self.num_holes = kwargs.get('num_holes',random_holes())

To better explain the concept of *args and **kwargs (you can actually change these names):
def f(*args, **kwargs):
   print 'args: ', args, ' kwargs: ', kwargs

>>> f('a')
args:  ('a',)  kwargs:  {}
>>> f(ar='a')
args:  ()  kwargs:  {'ar': 'a'}
>>> f(1,2,param=3)
args:  (1, 2)  kwargs:  {'param': 3}

"""










































