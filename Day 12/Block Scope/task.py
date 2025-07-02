global_var = "global variable"

def f():
    local_var = "local variable"
    print(local_var)
    print(global_var)

f()
if type(global_var) is str:
    global_var2 = "it is a global variable too"

print(global_var2)

# Coding exercise 11
def is_prime(num):
    half = num // 2
    for i in range(2, half + 1):
        if num % i == 0:
            return False
    return True