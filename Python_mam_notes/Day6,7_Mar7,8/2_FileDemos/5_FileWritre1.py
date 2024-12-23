# 5_FileWritre1.py

f = open('target.txt', 'w')
print(f.tell())
f.write('PSL')
print(f.tell())
f.close()
