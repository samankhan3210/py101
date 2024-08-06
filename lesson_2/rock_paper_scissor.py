'''Rock, Paper, and Scissors game with a new variation of Lizard and Spock '''
import random

CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
CHOICES_SHORTENED = ['r', 'p', 'sc', 'l', 'sp']
SCORES = {
    'user' : 0,
    'computer' : 0
}
MAX_SCORE = 3
MAX_ROUNDS = 5
WINNING_COMBOS = {
    'rock' : {'lizard', 'scissors'},
    'scissors' : {'paper', 'lizard'},
    'paper' : {'rock', 'spock'},
    'lizard' : {'spock', 'paper'},
    'spock' : {'scissors', 'rock'}
}

def welcome():
    '''prints a welcome message'''
    print("---- Welcome to the game of Rock, Paper, Scissors, Lizard, and Spock ----")

def goodbye():
    '''prints a goodbye message'''
    print("---- Goodbye! ----")

def get_user_choice():
    '''gets user choice for the game'''
    user_choice = ""
    combined_choices = [f"{l1} ({l2})" for l1, l2 in zip(CHOICES, CHOICES_SHORTENED)]
    while user_choice not in CHOICES:
        user_choice = input(f'Choose one from - {", ".join(combined_choices)} : ')
        user_choice = user_choice.lower().strip()
        if user_choice in CHOICES_SHORTENED:
            user_choice = CHOICES[CHOICES_SHORTENED.index(user_choice)]

    return user_choice

def is_winning_choice(u_choice, c_choice):
    '''checks for the dictionary for valid winning combos '''
    return c_choice in WINNING_COMBOS[u_choice]

def determine_round_winner(ur_choice, comp_choice):
    '''makes the decision to determine who won the game 
    based on the output of game rules function'''
    decission = ""

    if ur_choice == comp_choice:
        decission = "It's a tie!"
    elif is_winning_choice(ur_choice, comp_choice):
        decission = "You win!"
    else:
        decission = "Computer wins!"
    return decission

def update_winner_score(win):
    '''increments the score of the winner based on the decision'''
    if win == "You win!":
        SCORES['user'] += 1
    elif win == "Computer wins!":
        SCORES['computer'] += 1
    else:
        pass

def print_scores():
    '''prints game scores'''
    print(f"Your Score = {SCORES['user']}\nComputer's Score = {SCORES['computer']}\n")

def print_grand_winner():
    '''prints a message for the user whether he/she is a grand winner or not'''
    if SCORES['user'] == MAX_SCORE  or SCORES['user'] > SCORES['computer']:
        print("CONGRATULATIONS! YOU ARE THE GRAND WINNER. :)")
    elif SCORES['computer'] == MAX_SCORE or SCORES['computer'] > SCORES['user'] :
        print("ALAS! COMPUTER IS THE GRAND WINNER. :(")
    else:
        print('--- IT IS A TIE! :) ---')

def best_of_five(round_no):
    '''checks whether 5 rounds have comepleted or any user has reached a score of 3'''
    return SCORES['computer'] != MAX_SCORE and SCORES['user'] != MAX_SCORE \
        and round_no != MAX_ROUNDS

def main():
    '''main function'''
    round_number = 0
    welcome()
    while best_of_five(round_number):
        print(f"\n---- Round - {round_number + 1} ----")
        your_choice = get_user_choice()
        computer_choice = random.choice(CHOICES)
        print(f"Your choice = {your_choice}\nComputer's choice = {computer_choice}")
        winner = determine_round_winner(your_choice, computer_choice)
        print(winner)
        update_winner_score(winner)
        round_number += 1
        print_scores()

    print("---- FINAL SCORES ----")
    print_scores()
    print_grand_winner()
    goodbye()

if __name__ == "__main__":
    main()
    