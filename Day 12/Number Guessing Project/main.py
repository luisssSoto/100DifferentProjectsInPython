'''To do list
1. choose a random number
2. change the number of tries accordingly with the level of difficulty
3. react accordingly with the number chosen by the user
4. if the user guess the number before the number of tries win else loose '''

import art
import random

print(art.my_logo)
print("Welcome to the Number Guessing Game!", "I'm thinking of a number between 1 and 100.", sep="\n")

mistery_num = random.randint(1, 100)
was_number_guessed = False

while not was_number_guessed:
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    valid_answer = False
    if difficulty_level == "easy" or difficulty_level == "hard":
        valid_answer = True
    while not valid_answer:
        print("answer no valid, try again")
        difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard':")
        if difficulty_level == "easy" or difficulty_level == "hard":
            valid_answer = True
    number_of_tries = 0
    if difficulty_level == "easy":
        number_of_tries = 10
    else:
        number_of_tries = 5
    count_attempts = 0
    while count_attempts < number_of_tries:
        print(f'You have {number_of_tries - count_attempts} attempts remaining to guess the number.')
        guessed_number = int(input("Make a guess: "))
        if guessed_number == mistery_num:
            was_number_guessed = True
            result = f"You got it! The answer was {mistery_num}."
            print(result)
            break
        elif guessed_number > mistery_num:
            result = "Too high."
        else:
            result = "Too low."
        count_attempts += 1
        if count_attempts == number_of_tries:
            was_number_guessed = True
            result = "You've run out of guesses. Refresh the page to run again."
            print(result)
            break
        print(result)
        print("Guess again!")





