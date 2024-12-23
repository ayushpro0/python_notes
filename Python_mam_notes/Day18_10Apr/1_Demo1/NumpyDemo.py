import pandas as pd
a={'a':1,'b':2,'c':3}
b={'x':1,'y':2,'z':3}
x=pd.DataFrame(a,b)

print(x[:])
print('*'*50)
print(x[:1])