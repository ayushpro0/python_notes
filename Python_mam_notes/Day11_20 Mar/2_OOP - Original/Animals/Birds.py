class Birds:
    
    def __init__(self):         #constructor
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Sparrow', 'Robin', 'Duck']   #members is an instance property
 
 
    def printMembers(self):         #instance method
        print('Printing members of the Birds class')
        for member in self.members:
           print('\t%s ' % member)

#---------------------------------------------------------------------
if __name__  == "__main__":   #this is True if this current module file is executed on its own
    b1 =Birds()   # __init__(memory) method is called automatically
    b1.printMembers()

    #b2 = Birds(["a","b"])   #how many parameters passed 2 --(object, [a,b])
