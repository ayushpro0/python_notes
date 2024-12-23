# default arguments
# def calculate_tax(rate=0.2, cost ):  #SyntaxError

def calculate_tax(cost, rate=0.2):  # rate=0.2 is default argument  , cost is non default argument
    final_cost = cost + (cost * rate)  # cost , rate are local variables
    return final_cost


# main program
final_tax = calculate_tax(1000)  # called the func only with 1 argument
print("Tax with Default rate 0.2 = ", final_tax)

final_tax1 = calculate_tax(1000, 0.5)  # called the func with 2 arguments
print("Tax with rate 0.5 passed value = ", final_tax1)

final_tax = calculate_tax()  # TypeError: calculate_tax() missing 1 required positional argument: 'cost'
print("END!!!!")

"""
Question
from Amit to Sakshi Jamgaonkar (privately):
is it mandatory to have default argument mentioned at last? ---YES
"""
