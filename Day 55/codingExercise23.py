# TODO: Create the logging_decorator() function 👇
def logging_decorator(fun):
    def wrapper(*args):
        res = fun(*args)
        print(f"You called {fun.__name__}{args}")
        print(f"It returned: {res}")
        return res
    return wrapper


# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)

a_function(1, 2, 3)
