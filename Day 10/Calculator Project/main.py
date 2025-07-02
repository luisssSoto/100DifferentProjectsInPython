def add(n1, n2):
    return n1 + n2

# 1.
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# 2.
operations_dict = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

# 3.
mul = operations_dict["*"]
print(mul(4, 8))

import art
print(art.logo)

restart = True
first_operand = float(input("What's the first number?: "))
while restart:
    operation = input("+\n-\n*\n/\nPick an operation?: ")
    operation_chosen = operations_dict[operation]
    second_operand = float(input("What's the next number?: "))
    result = operation_chosen(first_operand, second_operand)
    print(f"{first_operand} {operation} {second_operand} = {result}")
    restart = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: or 'e' to exit the program?: ").lower()
    if restart == 'e':
        restart = False
    elif restart == 'y':
        restart = True
        first_operand = result
    else:
        restart = True
        print("\n" * 100)
        print(art.logo)
        first_operand = float(input("What's the first number?: "))