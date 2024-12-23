'''6.	Write a Python program to get the maximum and minimum value in a dictionary.
Consider sample Input dictionary as my_dict={'x':500,'y':5874,'z':560}
Sample output expected - Sample Output:
	Maximum Value:  5874                                                                                          
	Minimum Value:  500
Hint: use max(), lambda
'''
my_dict={'x':500,'y':5874,'z':560}
max_val = 1
min_val = (2**31-1)

for i in my_dict:
    if max_val < my_dict[i]:
        max_val = my_dict[i]

    if min_val> my_dict[i]:
        min_val = my_dict[i]    

print("maximum value: ", max_val)
print("minimum value: ", min_val)