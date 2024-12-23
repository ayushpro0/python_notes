class oPair:    # ordered pair
    
    def __init__(self, obj1, obj2):  # constructor
        self.data = (obj1, obj2)     # assign attribute , data is a tuple (6, -4)

    def __str__(self):              #pre-defined method - overidding
        return str(self.data)
    
    __repr__ = __str__              #__repr__ will automatically be printed when resolved on python prompt
    """
    def __repr__(self):
        return str(self.data)
    """
    #-------------------------------------------------
myPair = oPair(6, -4) 	# create instance  in all 3 parameters are passed-current memory,6,-4
print ("myPair = ", myPair)   #calls myPair.__str__()
#default str presenataion is <__main__.oPair instance at 0x0000000002F62108>



















"""
def __str__(self):# str() string representation
        return str(self.data) 	        # convert tuple to string

    __repr__ = __str__ 		# repr() string representation  outside this current module

    

"""























#calls repr() when u try to print at shell>>>myPair
"""
__repr__ = __str__ 		# repr() string representation
"""
