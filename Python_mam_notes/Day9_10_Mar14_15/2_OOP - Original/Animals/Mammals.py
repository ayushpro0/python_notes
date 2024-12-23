class Mammals:
    def __init__(self):
        """ Constructor for this class. """
        # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild Cat']

    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s ' % member)


"""
m1 = Mammals()
print "Mammals class instance variable = ",m1.members[0]
m1.members.append("XYZ")
print "Mammals class instance variable = ",m1.members


m1 = Mammals()
m1.printMembers()
"""
