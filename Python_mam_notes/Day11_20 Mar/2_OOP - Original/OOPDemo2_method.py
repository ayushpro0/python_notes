class SayHello:
    def __init__(self):        #constructor
        self.greeting = "Hello, how are you"

                  # define the method
    def display(self):                         #
        print ('You invoked method display()!')
        print ("Grreting = ", self.greeting)

print ("--------------------------------------------------")
obj1 = SayHello()   #instance created
print (obj1.greeting)  #accessing instance property
obj1.display()   #invoke instance method, current object itself is passed as an argumnet to that fun call
print ("-----------------------------------------------------")
obj2 = SayHello()
obj2.display()

print ("END!!!!")

















"""
  def display(self, num):
        print 'You invoked method display() with 1 parameter!'
        print "Grreting = ", num
"""
