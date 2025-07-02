# Higher Lower Game
# 1. import logo. Done
# 2. import the a data. Done
# 3. print the first statement. Done
# 4. print the next logo. Done
# 5. print the second statement. Done
# 6. create a function to compare the followers. Done
# 7. create a function to react according the input from the user. Done
# 8. create a var to keep track the user's score. Done
# Note: fix the famous_introduction method there are two A. Done
# 9. create a while to put all the game inside in it. Done
# 10 increasing score. Done
# 10. a keep track the B famous 'cause it will be the A famous the next time. Done
# 11. not select the same famous.

import art, random, game_data

def famous_introduction(famous, a_or_b):
    if a_or_b:
        introduction = f'Compare A: {famous["name"]} a {famous["description"]}, from {famous["country"]}.'
    else:
        introduction = f'Against B: {famous["name"]} a {famous["description"]}, from {famous["country"]}.'
    return introduction


def who_is_more_famous(user_decision, celebrity_a, celebrity_b):
    """it returns who famous has most followers"""
    if user_decision["name"] == celebrity_a["name"]:
        celebrity_a = user_decision
    elif user_decision["name"] == celebrity_b["name"]:
        celebrity_b = user_decision
    if celebrity_a["follower_count"] > celebrity_b["follower_count"]:
        winner = celebrity_a
    else:
        winner = celebrity_b
    return winner

def get_user_famous(user_decision, followers_a, followers_b):
    """it returns the decision which was made by the user"""
    user_decision = user_decision.upper()
    if user_decision == 'A':
        return followers_a
    elif user_decision == 'B':
        return followers_b
    else:
        return 'Answer not Valid'

def check_results(user_decision, winner):
    """it adds 1 point if the user's answer is right"""
    if user_decision["name"] == winner["name"]:
        return True
    else:
        return False

def choosing_famous(celebrities, data, celebrity_a, celebrity_b):
    """it returns a list of the next celebrities"""
    celebrity_a = celebrity_b
    celebrity_b = random.choice(data)
    celebrities.append(celebrity_a)
    celebrities.append(celebrity_b)
    return celebrities

def check_repeat_famous(celebrities, data):
    """it checks if there are repeated celebrities"""
    while celebrities[0]["name"] == celebrities[1]["name"]:
        del celebrities[1]
        celebrity_b = random.choice(data)
        celebrities.append(celebrity_b)

user_score = 0
is_over = False
famous_list = []

famous_a = random.choice(game_data.data)
famous_b = random.choice(game_data.data)
famous_list.append(famous_a)
famous_list.append(famous_b)
check_repeat_famous(famous_list, game_data.data)

while not is_over:
    logo = art.logo
    print(logo)
    famous_a = famous_list[0]
    is_famous_a_selected = True
    print(famous_introduction(famous_a, is_famous_a_selected))
    is_famous_a_selected = False
    print(art.vs)
    famous_b = famous_list[1]
    print(famous_introduction(famous_b, is_famous_a_selected))
    user_guess = input("Who has more followers? Type 'A' or 'B': ")
    user_famous = get_user_famous(user_guess, famous_a, famous_b)
    winner_famous = who_is_more_famous(user_famous, famous_a, famous_b)
    if check_results(user_famous, winner_famous):
        user_score += 1
        print(f"You're right! Current score: {user_score}")
        for _ in range(2):
            del famous_list[0]
        next_celebrities = choosing_famous(famous_list, game_data.data, famous_a, famous_b)
        check_repeat_famous(famous_list, game_data.data)
        print("\n" * 20)
    else:
        is_over = True
        print(f"Sorry, that's wrong. Final score: {user_score}")

