"""
6.	Write a Python program to get the maximum and minimum value in a dictionary.
Consider sample Input dictionary as my_dict={'x':500,'y':5874,'z':560}
Sample output expected - Sample Output:
	Maximum Value:  5874                                                                                          
	Minimum Value:  500
Hint: use max(), lambda

"""
my_dict = {'x': 500, 'y': 5874, 'z': 560}

max_val = max(my_dict.items(), key=lambda x: x[1])
min_val = min(my_dict.items(), key=lambda x: x[1])

print(f"Maximum Value: {max_val[1]}")
print(f"Minimum Value: {min_val[1]}")
