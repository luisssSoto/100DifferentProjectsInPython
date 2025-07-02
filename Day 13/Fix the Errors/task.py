try:
    age = int(input("How old are you?"))
except ValueError:
    print("try again. only numerical values are allowed")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
else:
    print(f"You can not drive because your age is {age}.")





