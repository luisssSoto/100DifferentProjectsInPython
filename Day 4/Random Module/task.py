import random

# randint()
print(random.randint(1, 10))

# random()
print(random.random())
print(random.random() * 10)

# uniform()
print(random.uniform(1, 10))

if random.randint(1,2) == 1:
    print("Heads")
else:
    print("Tails")