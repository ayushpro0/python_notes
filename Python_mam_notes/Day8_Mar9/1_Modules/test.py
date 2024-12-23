# Import classes from your brand-new package_example
# import Animals
# Animals.Birds

from Animals import Mammals
from Animals import Birds

# Create an object of Mammals class & call a method of it
myMammal = Mammals()
myMammal.printMembers()

# Create an object of Birds class & call a method of it
myBird = Birds()
myBird.printMembers()

"""
installing module in Python
>pip install module_name
"""
