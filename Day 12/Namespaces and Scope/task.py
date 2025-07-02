enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope
def drink_potion():
    potion_to_drink = 'superpotion'
    print(f"potion to drink: {potion_to_drink}")

drink_potion()
try:
    print(potion_to_drink)
except NameError as e:
    print(f'error: {e}')

# Global Scope
player_health = 100

def show_health():
    return player_health

print(show_health())
print(player_health)

# Note: each element which has a name (variables, functions, methods, etc) has a
# namespace and each namespace has a scope where it is valid that element

'''A namespace is a named declarative region that helps organize 
code and prevent naming conflicts. 
Scope, on the other hand, refers to the region of a program where a 
particular identifier (like a variable or function name) is valid 
and can be accessed'''