# positional parameter   / non- keyword arguments/ non default argumnents

def hello(name):
    """Parameter passing"""
    print("Hello " + name)
    # return ""  #function return None as default return value


result = hello("Python")  # invoking the function
print("Return value = ", result)  # None

print("------------------------------------------------------")

# result = hello()           #TypeError: hello() missing 1 required positional argument: 'name'
result = hello("abc", 100)  # TypeError: hello() takes 1 positional argument but 2 were given
print("END!!!!")
