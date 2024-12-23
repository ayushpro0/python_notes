print("Output of range(5) = ", range(5))  # Output of range(5) =  range(0, 5)
print("Output of range(5,11) = ", range(5, 11))  # Output of range(5) =  range(5, 11)
print("Output of range(5,11,2) = ", range(5, 11, 2))  # Output of range(5,11,2) = range(5, 11, 2)

print("---------------------------------------------------------------------------------------------")

x = [1.0, 2.0, 3.0]
for n in x:
    print(n)
    n = n ** 2

print("updated x =", x)  # this is not updated [1.0, 2.0, 3.0]

print("--------------------------------------------")

# for and range
x = [1, 3, -7, 4, 9, -5, 4]
for i in range(len(x)):  # range(7)    [0,1,2,3,4,5,6]
    if x[i] < 0:
        print("Found a negative number", x[i], " at index ", i)

"""
Sometimes there arises a need to loop with explicit indices to use the position at which values occur in a list.
The range function can be used in such scenarios. 

"""
