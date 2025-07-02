rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
items = [rock, paper, scissors]
user_choose = items[int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))]
computer_choose = items[random.randint(0, 2)]
results = ''
if user_choose == rock:
    if computer_choose == rock:
        results = "It's draw"
    elif computer_choose == paper:
        results = "You lose"
    elif computer_choose == scissors:
        results = "You win"
elif user_choose == paper:
    if computer_choose == rock:
        results = "You win"
    elif computer_choose == paper:
        results = "It's draw"
    elif computer_choose == scissors:
        results = "You lose"
elif user_choose == scissors:
    if computer_choose == rock:
        results = "You lose"
    elif computer_choose == paper:
        results = "You win"
    elif computer_choose == scissors:
        results = "It's draw"

print(f"{user_choose}\nComputer choose:\n{computer_choose}\n{results}")