
# f = open('data11.txt', "r")   #by default read mode
# f = open('data11.txt')   # by default read mode #IOError:


f = open('data.txt')  # by default read mode #IOError:
while True:
        char = f.read(1)
        if not char: break
        print (char)
f.close()







"""
#as opposed to
for char in open('data.txt').read():
        print char
"""
