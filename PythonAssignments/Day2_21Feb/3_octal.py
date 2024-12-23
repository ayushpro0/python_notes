# 3.	Convert Decimal number to octal using print() output formatting
# (Hint: Just 1 line code)


num = int(input("Enter a number to converted in Octal form \n"))

oct_num = oct(num)
print("Octal Form of {} is {} ".format(num, oct_num))

# OR

print("%.3o" % num)
