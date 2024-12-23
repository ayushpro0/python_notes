import math

Ax = int(input("Enter the x-coordinate of vertex A\n"))
Ay = int(input("Enter the y-coordinate of vertex A\n"))
Bx = int(input("Enter the x-coordinate of vertex B\n"))
By = int(input("Enter the y-coordinate of vertex B\n"))
Cx = int(input("Enter the x-coordinate of vertex C\n"))
Cy = int(input("Enter the y-coordinate of vertex C\n"))

dAB = math.sqrt((Bx - Ax)**2 + (By - Ay)**2)
print("Length of side AB is %0.1f" %dAB)

dBC = math.sqrt((Cx - Bx)**2 + (Cy - By)**2)
print("Length of side BC is %0.1f" %dBC)

dAC = math.sqrt((Cx - Ax)**2 + (Cy - Ay)**2)
print("Length of side CA is %0.1f" %dAC)
