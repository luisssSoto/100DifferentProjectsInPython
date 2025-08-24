"""*args parameter Unlimited Positional Arguments"""

def add(*args):
    result = 0
    for arg in args:
        result += arg
    print(type(args))
    return result

print(add(1,2,3,4,5,6,7,8,9,10))