import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1. approach
random_index = random.randint(0, len(friends) - 1)
print(friends[random_index])

# 2. approach
print(random.choice(friends))
