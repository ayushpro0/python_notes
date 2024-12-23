s1 = "100"
num1 = int(s1)
print("s1 = ", s1, "type = ", type(s1), "ID = ", id(s1))
# s1 =  100 type =  <class 'str'> ID =  2395258401264

print("num1 = ", num1, "type = ", type(num1), "ID = ", id(num1))

print("---------------------------------------------------------------")

s1 = "abc"
print("s1 = ", s1, "type = ", type(s1), "ID = ", id(s1))
# s1 =  abc type =  <class 'str'> ID =  2395258306416

# num1 = int(s1) #ValueError: invalid literal for int() with base 10: 'abc'
print("num1 = ", num1, "type = ", type(num1), "ID = ", id(num1))
