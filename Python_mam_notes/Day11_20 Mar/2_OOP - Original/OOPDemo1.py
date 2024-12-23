class SayHello:                 #class def
    
    def __init__(self):       #constructor
        print ("Self object = ",self)
        self.greeting = "Hello, how are you"    #greeting is instance var

    #insatnce method
#-------------------------------------------------------

        
hello1 = SayHello()             #creating an object of class SayHello, it by default calls __init__(self)
print ("object = ",hello1)
print (hello1.greeting)           #accessing instance var greeting
print ("------------------------------------------------------")


hello2 = SayHello()             #creating an object of class SayHello
print (hello2.greeting)           #accessing instance var greeting
