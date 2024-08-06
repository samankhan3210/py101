'''Rock, Paper, and Scissors game with a new variation of Lizard and Spock '''
import os
import random

CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
CHOICES_SHORTENED = ['r', 'p', 'sc', 'l', 'sp']
COMBINED_CHOICES = [f"{l1} ({l2})" for l1, l2 in zip(CHOICES, CHOICES_SHORTENED)]
PLAY_AGAIN_OPTIONS = ['y', 'yes', 'n', 'no']
YES_OPTIONS = ['y', 'yes']
COMPUTER_WINS = 0
USER_WINS = 0
RULES_DICT = {
    'rock' : {'lizard', 'scissors'},
    'scissors' : {'paper', 'lizard'},
    'paper' : {'rock', 'spock'},
    'lizard' : {'spock', 'paper'},
    'spock' : {'scissors', 'rock'}
}

def game_rules(u_choice, c_choice):
    '''checks for the dictionary for valid winning combos '''
    return c_choice in RULES_DICT[u_choice]

def winner_func(ur_choice, comp_choice):
    '''makes the decision to determine who won the game 
    based on the output of game rules function'''
    decission = ""

    if ur_choice == comp_choice:
        decission = "It's a tie!"
    elif game_rules(ur_choice, comp_choice):
        decission = "You win!"
    else:
        decission = "Computer wins!"
    return decission

def game_count(win):
    '''increments the score of the winner based on the decision'''
    global USER_WINS, COMPUTER_WINS
    if win == "You win!":
        USER_WINS += 1
    elif win == "Computer wins!":
        COMPUTER_WINS += 1
    else:
        pass

def grand_winner():
    '''prints a message for the user whether he/she is a grand winner or not'''
    if USER_WINS == 3:
        print("CONGRATULATIONS! You are the GRAND WINNER.")
    elif COMPUTER_WINS == 3:
        print("ALAS! COMPUTER IS the GRAND WINNER.")
    else:
        print("Bye!")

AGAIN = "y"
while AGAIN.lower() in YES_OPTIONS :
    os.system('cls || clear')
    user_choice = input(f'Choose one from - {", ".join(COMBINED_CHOICES)} : ')
    user_choice = user_choice.lower()
    while user_choice not in CHOICES:
        user_choice = input(f'Choose one from - {", ".join(COMBINED_CHOICES)} : ')
        user_choice = user_choice.lower()
        if user_choice in CHOICES_SHORTENED:
            user_choice = CHOICES[CHOICES_SHORTENED.index(user_choice)]
        print(user_choice)

    computer_choice = random.choice(CHOICES)
    print(f"Your choice = {user_choice}\nComputer's choice = {computer_choice}")
    WINNER = winner_func(user_choice, computer_choice)
    print(WINNER)
    game_count(WINNER)
    print(f"Your score : {USER_WINS}\nComputer Score : {COMPUTER_WINS}")
    AGAIN = "dummy"

    if USER_WINS < 3 and COMPUTER_WINS < 3:
        while AGAIN.lower() not in PLAY_AGAIN_OPTIONS:
            AGAIN = input("Do you want to play again (y/n)? ")
            if AGAIN.lower() not in PLAY_AGAIN_OPTIONS:
                print("Incorrect Option, Try Again! ")
grand_winner()
    