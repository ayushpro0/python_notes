f = open('target.txt', "w")
f.write("hello World\n")
f.close()

f = open("target.txt")  # by default read mode
while True:
    str = f.readline()
    print("position in loop = ", f.tell())
    if str:
        print(str)
    else:
        break
print("----------------------------------------------")  # f is pointing at the end of file
f.seek(5)  # absolute positioning from beginning of a file
print("Current position = ", f.tell())  # 5
print(f.read())  # " World\n"
f.close()
