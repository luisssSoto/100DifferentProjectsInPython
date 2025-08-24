"""** kwargs parameter """

def f (n, **kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value, sep="|")
    print(f"addition: {n + kwargs["add"]}")
    print(f"multiplication: {n * kwargs["mul"]}")
    print(f"subtraction: {n - kwargs["sub"]}")
    print(f"division: {n / kwargs["div"]}")


print(f(n = 10, add = 2, mul = 3, sub = 4, div = 2))


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]
        # the method get helps us to don't raise any Error if the element doesn't exist
        self.year = kwargs.get("year")

my_car = Car(make="Ford", model="Mustang")
print(my_car.make)
print(my_car.model)
print(my_car.year)


def having_fun(n, *args, **kwargs):
    print(n, args, kwargs)

having_fun(1, 2, 3, 4, first=1, second=2)