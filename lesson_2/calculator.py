''' simple calculator code that accepts two numbers 
and perfroms simple calculations on them '''
import json
import os

LANGUAGES_LIST = ['urdu', 'ur', 'u', '1', '2', 'en', 'e', 'english']
CHOICE_OPTIONS = ['y', 'yes', 'yep', 'n', 'no', 'nope']
VALID_CALCULATION_OPTIONS = ["1", "2", "3", "4", "+", "-", "x", "/"]

with open('calculator_messages.json', 'r', encoding='utf-8') as file:
    MESSAGES = json.load(file)

def number_validation(prompt):
    '''validates that the number is a float and not a string'''
    while True:
        try:
            number = float(input(prompt))
            break
        except ValueError:
            print(MESSAGES[LANGUAGE]['invalid_number'])

    return number

while True:
    LANGUAGE = input(MESSAGES['lang'])
    if LANGUAGE.lower() not in LANGUAGES_LIST:
        print(MESSAGES['en']['invalid_number'])
    else:
        if LANGUAGE.lower() in ['urdu', 'ur', 'u', '1']:
            LANGUAGE = 'ur'
        else:
            LANGUAGE = 'en'
        break

while True:
    os.system('cls')
    number1 = number_validation(MESSAGES[LANGUAGE]['number_1'])
    number2 = number_validation(MESSAGES[LANGUAGE]['number_2'])
    while True:
        operation = input(MESSAGES[LANGUAGE]['operation_prompt'])

        if operation in VALID_CALCULATION_OPTIONS:
            break

        print(MESSAGES[LANGUAGE]['invalid_operation'])

    OUTPUT = 0
    if operation in ["1", "+"]:
        OUTPUT = float(number1) + float(number2)
    if operation in ["2", "-"]:
        OUTPUT = float(number1) - float(number2)
    if operation in ["3", "x"]:
        OUTPUT = float(number1) * float(number2)
    if operation in ["4", "/"]:
        try:
            OUTPUT = float(number1) / float(number2)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero")

    OUTPUT = round(OUTPUT, 2)
    print(MESSAGES[LANGUAGE]['result'].format(answer=OUTPUT))
    while True:
        choice = input(MESSAGES[LANGUAGE]['another_operation'])
        choice = choice.lower()
        if choice not in CHOICE_OPTIONS:
            print(MESSAGES[LANGUAGE]['invalid_number'])
        else:
            break

    if choice[0] == 'n':
        break
