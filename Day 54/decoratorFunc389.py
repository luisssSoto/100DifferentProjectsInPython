"""Decorator function is a function that has a nested function (wrapper function)
that adds more functionality to the functions that was passed as argument"""

import time
def delay_decorator(fun):
    def wrapper_func():
        time.sleep(3)
        # Do something before
        fun()
        # Do something later
    return wrapper_func

@delay_decorator
def say_hi():
    print("hi")

def say_bye():
    print("bye")

say_hi()
say_bye()

# Without decorator
def introduction():
    print("my name is Alex")

intro = delay_decorator(introduction)
intro()

