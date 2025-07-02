# Modifying Global Scope

enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

a = 0
def modify_a():
    global a
    a -= 1
    return a
print(modify_a())
print(a)


