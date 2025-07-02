# range(a)
for i in range(5):
    print(i, end=' ')
print()

# range(a, b)
for i in range(2, 5):
    print(i, end=' ')
print()

# range(a, b, c)
for i in range(1, 5, 2):
    print(i, end=' ')
print()

# 1. Gauss Challenge
total = 0
for i in range(1, 101):
    total += i
print(total)