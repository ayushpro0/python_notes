

class SayHello:
    def __init__(self, msg):        #parameterised constructor
        self.greeting = msg

                  # define the method
    def display(self):
        print ('You invoked method display()!')
        print ("Greeting = ", self.greeting)
    """
    def display(self,s1):
        print ('You invoked method display()!')
        print ("Greeting = ", self.greeting)
        print ("s1 = ",s1)
    """

  
print ("--------------------------------------------------")
obj1 = SayHello("Hello!!")   #instance created, 2 parameters are passed (self,"Hello!!!")
print ("obj1.greeting = ",obj1.greeting)  #accessing instance property
obj1.display()   #invoke instance method, current object itself is passed as an argumnet to that
                #func call

#obj1.display("Python")   #TypeError: display() takes 1 positional argument but 2 were given
print ("--------------------------------------")

obj2 = SayHello("Good Bye!!")   #instance created, 2 parameters are passed (self,"Hello!!!")
print ("obj2.greeting = ",obj2.greeting)  #accessing instance property
obj2.display()   #invoke instance method, current object itself is passed as an argumnet to that func call







"""
             # define the method
    def display(self):
        print 'You invoked method display()!'
        print "Greeting = ", self.greeting
"""









"""
  def display(self, num):
        print 'You invoked method display() with 1 parameter!'
        print "Grreting = ", num
"""
