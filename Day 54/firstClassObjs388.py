"""First class objects (functions) can be passed as arguments"""
def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

def calculate(operation, n1 ,n2):
    return operation(n1, n2)

result = addition(1, 2)
print(result)
print()

"""Functions can be nested"""
def outer_func():
    print("outer function")
    def inner_func():
        print("inner function")
    inner_func()
outer_func()
print()

"""Functions can be returned"""
def out_func():
    print("out")
    def in_func():
        print("in")
    return in_func

result = out_func()
result()
