'''Rock, Paper, and Scissors game with a new variation of Lizard and Spock '''
import random

CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
CHOICES_SHORTENED = ['r', 'p', 'sc', 'l', 'sp']
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

def update_winner_score(win, score):
    '''increments the score of the winner based on the decision'''
    if win == "You win!":
        score['user'] += 1
    elif win == "Computer wins!":
        score['computer'] += 1
    else:
        pass

def print_scores(score):
    '''prints game scores'''
    print(f"Your Score = {score['user']}\nComputer's Score = {score['computer']}\n")

def print_grand_winner(score):
    '''prints a message for the user whether he/she is a grand winner or not'''
    if score['user'] == MAX_SCORE  or score['user'] > score['computer']:
        print("CONGRATULATIONS! YOU ARE THE GRAND WINNER. :)")
    elif score['computer'] == MAX_SCORE or score['computer'] > score['user'] :
        print("ALAS! COMPUTER IS THE GRAND WINNER. :(")
    else:
        print('--- IT IS A TIE! :) ---')

def best_of_five(round_no, score):
    '''checks whether 5 rounds have comepleted or any user has reached a score of 3'''
    return score['computer'] != MAX_SCORE and score['user'] != MAX_SCORE \
        and round_no != MAX_ROUNDS

def main():
    '''main function'''
    round_number = 0
    welcome()
    score = {
    'user' : 0,
    'computer' : 0
    }
    while best_of_five(round_number, score):
        print(f"\n---- Round - {round_number + 1} ----")
        your_choice = get_user_choice()
        computer_choice = random.choice(CHOICES)
        print(f"Your choice = {your_choice}\nComputer's choice = {computer_choice}")
        winner = determine_round_winner(your_choice, computer_choice)
        print(winner)
        update_winner_score(winner, score)
        round_number += 1
        print_scores(score)

    print("---- FINAL SCORES ----")
    print_scores(score)
    print_grand_winner(score)
    goodbye()

if __name__ == "__main__":
    main()
    