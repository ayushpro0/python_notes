# def add(num1, num2, **y, *x): # SyntaxError:

# proper syntax:  non default, default, *,**

def add(num1, num2, *x, **y):
    print("x = ", x, "type = ", type(x))  # x =  () type =  <class 'tuple'>
    print("y = ", y, "type = ", type(y))  # y =  {'x1': 100, 'y1': 100} type =  <class 'dict'>
    print("y[x1] = ", y["x1"])  # y[x1] =  100
    return num1 + num2


print("Functions Learning....")

add(1, 2, x1=100, y1=100)
