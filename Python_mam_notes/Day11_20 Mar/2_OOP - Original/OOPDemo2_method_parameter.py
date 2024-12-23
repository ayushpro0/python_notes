class SayHello:
    def __init__(self, msg):        #constructor
        '''Parameterised constructor'''
        self.greeting = msg
                  # define the method
    def display(self):                         #
        print ('You invoked method display()!')
        print ("Grreting = ", self.greeting)
print ("--------------------------------------------------")
obj1 = SayHello("Hello EveryOne !!!!!")   #instance created
print ("obj1.greeting = ",obj1.greeting)  #accessing instance property
obj1.display()   #invoke instance method, current object itself is passed as an argumnet to that fun call
print ("-----------------------------------------------------")
#obj2 = SayHello()   TypeError
obj2 = SayHello("Learning Python!!Interesting!!!!!")
obj2.display()
print ("END!!!!")

















"""
  def display(self, num):
        print 'You invoked method display() with 1 parameter!'
        print "Grreting = ", num
"""
