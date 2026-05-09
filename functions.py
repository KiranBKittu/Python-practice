# Defining functions in Python
""" def fun_name():
   print("Hai")
fun_name()

def mult(a: int, b: int)-> int:
    return a * b # Default None
res = mult(3.0, 3)
print(res) """

def mult(a, b, *args, **kwargs):
# *args ->pass any no: position arguments
# **kwargs ->pass any no: keyword arguments
    print(f"a:{a}, b:{b}, args:{args}, kwargs:{kwargs}")
    print(a,b, args, kwargs)
    return a * b # Default None
# a=4, b=5 are keyword arguments, as they contains keys and values
# '3.0', 3 are called positional arguments
res = mult('3.0', 3, 4, 5, c=8, d=9)
print(res)

# When we specify data type in function but if we give different data type when passing the values what will happen

#it won't consider what value we are giving, it is just like expose in docker, it will accepts all 

def abc(a: int, b: float)-> float:
    return a + b 
print(abc(1,2))

""" def calc(a,b, operation):
    if operation == "add":
        return a + b
    if operation == "sub":
        return a - b
    if operation == "mult":
        return a * b
    if operation == "div":
        return a / b
a, b = tuple(map(int, input("Enter 2 Numbers: ").split()))
operation = input("Enter operation to perform (add, sub, mult, div):")
res = calc(a, b, operation)
print(res) """

def f1(c,d, operation):
    if operation == "add":
        return c + d
    if operation == "sub":
        return c - d
c, d = tuple(map(int, input("Enter two values:").split()))
operation = input("Enter the operation:")
res = f1(c, d, operation)
print(res)
