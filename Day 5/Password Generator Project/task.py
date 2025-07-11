letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

# easy version
import random
letters_list = []
numbers_list = []
symbols_list = []
for i in range(nr_letters):
    letters_list.append(letters[random.randint(0, len(letters) - 1)])
for i in range(nr_numbers):
    numbers_list.append(numbers[random.randint(0, len(numbers) - 1)])
for i in range(nr_symbols):
    symbols_list.append(symbols[random.randint(0, len(symbols) - 1)])
user_password_list = []
user_password_list += letters_list + numbers_list + symbols_list
print(user_password_list)
user_password = ''
for character in user_password_list:
    user_password += character
print(user_password)
print()

# hard version
user_password = ''
random.shuffle(user_password_list)
print(user_password_list)
for character in user_password_list:
    user_password += character
print(f"Your password is: {user_password}")