import art
import random

cards = [i + 1 if i < 10 else 10 for i in range(13) for j in range(4)]

card_player_hand = []
card_dealer_hand = []
hands = [{'dealer' : card_dealer_hand}, {'player' : card_player_hand}]

def get_first_hand(deck, hand):
    """get the first user's and dealer's hand"""
    first_card_index = random.randint(0, len(deck) - 1)
    first_card = deck[first_card_index]
    get_rid_of_card(first_card_index, deck)
    hand.append(first_card)
    second_card_index = random.randint(0, len(deck) - 1)
    second_card = deck[second_card_index]
    hand.append(second_card)
    get_rid_of_card(second_card_index, deck)
    return hand

def show_user_results(hand):
    """show user's score"""
    return f"Your cards: {hand}, current score: {get_score(hand)}"

def show_dealer_results(hand):
    """show dealer's score"""
    return f"Dealer's first card: {hand[0]}"

def get_rid_of_card(index_of_card, deck):
    """it deletes any card take by the user or dealer"""
    for i in range(index_of_card, len(deck) - 1):
        deck[i] = deck[i + 1]
    del deck[-1]

def get_score(hand):
    """it gets the score of any hand"""
    if len(hand) == 2 and 10 in hand and 1 in hand:
        return 21
    score = 0
    for card in hand:
        score += card
    return score

def get_extra_card(deck, hand):
    "it gets an extra card and look if the hand went over or if get a Blackjack"
    extra_card_index = random.randint(0, len(deck) - 1)
    extra_card = deck[extra_card_index]
    right_hand = ''
    for key, value in hand.items():
        if key == 'dealer':
            right_hand = 'dealer'
        else:
            right_hand = 'player'
    hand[right_hand].append(extra_card)
    get_rid_of_card(extra_card_index, deck)
    if limit_score_was_passed(get_score(hand[right_hand])):
        looser = (who_went_over(right_hand))
        if looser == 'Dealer':
            print("Dealer went over!")
        else:
            print("You went over!")
        return 'The hand went over!'
    if getting_a_blackjack(hand[right_hand]):
        print(right_hand.title(), "get a blackjack!")
        return 'Blackjack!'
    return hand

def show_dealer_hand(dealer_hand):
    """shows the first card of the dealer to the user"""
    return dealer_hand[0]

def limit_score_was_passed(score):
    """check if the user has passed the score"""
    if score > 21:
        return True
    else:
        return False

def is_safety_take_a_card(dealer_hand):
    """logic of dealer to take another card"""
    if get_score(dealer_hand) < 17:
        return True
    else:
        return False

def who_went_over(right_hand):
    """check if someone went over"""
    looser = ''
    if right_hand == 'dealer':
        looser = 'Dealer'
    elif right_hand == 'player':
        looser = 'You'
    return looser

def declare_winner(dealer_hand, user_hand, player_went_over, dealer_went_over):
    """declare who wins"""
    if player_went_over == 'The hand went over!':
        print('You lose')
    elif dealer_went_over == 'The hand went over!':
        print('You win')
    else:
        if get_score(dealer_hand) > get_score(user_hand) or (dealer_hand == 21 and user_hand != 21):
            print('You lose')
        elif get_score(dealer_hand) < get_score(user_hand) or (user_hand == 21 and dealer_hand != 21):
            print('You win')
        else:
            print('Draw')

def end_of_the_match(dealer_hand, user_hand):
    """show the final results"""
    print(f"Your final hand: {user_hand}, final score: {get_score(user_hand)}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {get_score(dealer_hand)}")

def getting_a_blackjack(hand):
    """know if there is a blackjack"""
    result = False
    if (len(hand) == 2) and (10 in hand and 1 in hand):
        print("Natural Blackjack!")
        result = True
    elif get_score(hand) == 21:
        print("Non natural Blackjack!")
        result = True
    return result

def shuffle_deck(deck):
    """reset the deck"""
    deck = [i + 1 if i < 10 else 10 for i in range(13)for j in range(4)]
    return deck

def restart_game(user_hand, dealer_hand, deck):
    """restart the cards again and the game"""
    user_hand.clear()
    dealer_hand.clear()
    return shuffle_deck(deck)

continue_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
users_hand = []
dealers_hand = []
is_a_new_game = True
while continue_playing == 'y':
    if is_a_new_game:
        print(art.logo)
        users_hand = get_first_hand(cards, card_player_hand)
        dealers_hand = get_first_hand(cards, card_dealer_hand)
        if getting_a_blackjack(users_hand) or getting_a_blackjack(dealers_hand):
            continue_playing = 'n'
    if continue_playing != 'n':
        print(show_user_results(users_hand))
        print(show_dealer_results(dealers_hand))
        continue_playing = input("Type 'y' to get another card, type 'n' to pass: ")
    was_player_went_over = False
    was_dealer_went_over = False
    if continue_playing == 'y':
        was_player_went_over = get_extra_card(cards, hands[1])
        if was_player_went_over == 'The hand went over!' or was_player_went_over == 'Blackjack!':
            continue_playing = 'n'
    while is_safety_take_a_card(dealers_hand) and was_player_went_over != 'The hand went over!':
        was_dealer_went_over = get_extra_card(cards, hands[0])
        if was_dealer_went_over == 'The hand went over!' or was_dealer_went_over == 'Blackjack!':
            continue_playing = 'n'
    if continue_playing == 'n':
        end_of_the_match(dealers_hand, users_hand)
        declare_winner(dealers_hand, users_hand, was_player_went_over, was_dealer_went_over)
        continue_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if continue_playing == 'y':
            cards = restart_game(users_hand, dealers_hand, cards)
            is_a_new_game = True
            print(cards)
    else:
        is_a_new_game = False