import sys

temp = sys.stderr

sys.stderr = open("error.txt", "a")

print(nosuchvar) #error gets printed in file error.txt