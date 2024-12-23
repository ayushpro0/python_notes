from array import array

a = array('H', [4000, 10, 700, 22222]) # from module "array", array() function is called

print(a) # array('H', [4000, 10, 700, 2222])

print(sum(a)) #26932

print("-------------------------------------------")

print(dir(array))

print("-------------------------------------------")

array.reverse(a)
print(a) # array('H', [22222, 700, 10, 4000])

