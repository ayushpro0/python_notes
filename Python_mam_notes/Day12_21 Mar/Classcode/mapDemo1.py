


list1 = [10,20,30]
squarelist = [i**2 for i in list1 if type(i)==int]
print ("list1 = ", list1)
print("squarelist = ", squarelist)
print("----------------------------------------------")


#map() function
def squareElement(num1):            #Def
    return num1**2
result = squareElement(5)           #call to that func
print("Sqaure of 5 =", result)
    
mapObj = map(squareElement,list1)
print("mapObj = ", mapObj)#<map object at 0x101e22e30>
print("map list = ", list(mapObj))#[100, 400, 900]
"""
mapObj = map(
    squareElement(list1[0])->100
    squareElement(list1[1])->400
    squareElement(list1[2])->900
    ) --->   100 400 900

"""
print("----------------------------------------------")

r1 = lambda x : x**2
ans = r1(6)
print("square of 6 = ", ans)
(lambda x : x**2)(8)
print("----------------------------------------------")
#Alternative to above map call--->
squarelist2 = list(map(lambda x:x**2, list1))
print("squarelist2 = ", squarelist2)


"""
mapObj = map(
    lambda x : x**2
        (list1[0])->100
        (list1[1])->400
        (list1[2])->900
    ) --->   100 400 900

"""








