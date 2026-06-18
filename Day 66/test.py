class C():
    def __init__():
        super(ZeroDivisionError)
    
print(C)
c = C()
print(c)

try:
    print(3/1)
    raise ZeroDivisionError
except ZeroDivisionError as e:
    print(f"division error: {e}")