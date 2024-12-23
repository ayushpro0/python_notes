
"""
4.	Write a Python Program to add two matrices using nested loop.
Consider below 2 sample matrices.
X =     [[12,7,3],
        [4 ,5,6],
        [7 ,8,9]]
Y =     [[5,8,1],
        [6,7,3],
        [4,5,9]]
"""

X =     [[12,7,3],
        [4 ,5,6],
        [7 ,8,9]]
Y =     [[5,8,1],
        [6,7,3],
        [4,5,9]]
Z = []

for i in range(0, 3):
    row = []
    for j in range(0, 3):
        row.append(X[i][j] + Y[i][j])
    
    Z.append(row)

for i in Z:
    print(i)
