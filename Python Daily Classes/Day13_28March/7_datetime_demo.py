from datetime import date # class datetime is module file, data is class inside this file

now = date.today() #classmethod
print("Today is = ", now) # Today is =  2023-04-13

ord1 = now.toordinal() + 3 # day incremented by 3
print (date.fromordinal(ord1).strftime("%m-%d-%y")) # 04-16-23

print("----------------------------------------------------")

# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days) # 21440

print("-----------------------------------------------------")

print(dir(date))
