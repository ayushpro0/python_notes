# functional programming

list1 = [10, 20, 30, 40, "abc"]

squareList = [i**2 for i in list1 if type(i) == int]

print("squareList = ", squareList) # [100, 400, 900, 1600]

print("------------------------------------------")

#map() function
list1 = [10, 20, 30, 40]

def squareElement(num):
    return num**2

result = squareElement(5)
print("Square of 5 = ", result)

mapObj = map(squareElement, list1)
print("mapObj = ", mapObj) # <map object at 0x00000225C8A4BA90>
print("map list = ", list(mapObj)) # [100, 400, 900, 1600]

print("------------------------------------------")

r1 = lambda x : x**2
ans = r1(6)
print("square of 6 = ", ans) # 36

print("------------------------------------------")

# alternative to above using map call 
squarelist2 = list(map(lambda x : x**2, list1))
print("squarelist2 = ", squarelist2) # [100, 400, 900, 1600]