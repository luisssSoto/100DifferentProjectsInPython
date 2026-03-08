import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970

def speed_calc_decorator(fun):
    def wrapper_func():
        before = current_time
        fun()
        after = time.time()
        print(after - before)
    return wrapper_func

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i
    print(f"fast_function run speed: ", end=" ")

fast_function()

def slow_function():
    for i in range(10000000):
        i * i
    print("slow_function run speed: ", end=" ")

slow = speed_calc_decorator(slow_function)
slow()


# Different approach
import time


def speed_calc_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} run speed: {end_time - start_time}s")
        return result

    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()