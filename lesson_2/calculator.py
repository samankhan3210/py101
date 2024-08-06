''' simple calculator code that accepts two numbers 
and perfroms simple calculations on them '''
import json
import os

LANGUAGES_LIST = ['urdu', 'ur', 'u', '1', '2', 'en', 'e', 'english']
CHOICE_OPTIONS = ['y', 'yes', 'yep', 'n', 'no', 'nope', 'jee', 'nahi']
VALID_CALCULATION_OPTIONS = ["1", "2", "3", "4", "+", "-", "x", "/"]

with open('calculator_messages.json', 'r', encoding='utf-8') as file:
    MESSAGES = json.load(file)

def error_message(lang = 'en'):
    '''prints error message'''
    os.system('cls || clear')
    print(MESSAGES[lang]['error'])

def prompt_language():
    '''asks user for his/her language preference'''
    while True:
        language = input(MESSAGES['lang'])
        if language.lower().strip() not in LANGUAGES_LIST:
            error_message()
        else: 
            if language.lower().strip() in ['urdu', 'ur', 'u', '1']:
                language = 'ur'
            else:
                language = 'en'
            break
    return language

def welcome(lang = 'en'):
    '''prints a welcome message'''
    print(MESSAGES[lang]['welcome'])

def goodbye(lang = 'en'):
    '''prints a goodbye message'''
    print(MESSAGES[lang]['goodbye'])

def number_validation(prompt, lang = 'en'):
    '''validates that the number is a float and not a string'''
    while True:
        try:
            number = float(input(prompt))
            break
        except ValueError:
            print(MESSAGES[lang]['invalid_number'])

    return number

def prompt_number1(lang = 'en'):
    '''asks user for first number'''
    return number_validation(MESSAGES[lang]['number_1'])

def prompt_number2(lang = 'en'):
    '''asks user for second number'''
    return number_validation(MESSAGES[lang]['number_2'])

def prompt_operation(lang = 'en'):
    '''asks user for type of calculation'''
    while True:
        operation = input(MESSAGES[lang]['operation_prompt'])
        if operation in VALID_CALCULATION_OPTIONS:
            break
        else:
            error_message(lang)
    if operation in ["1", "+"]:
        operation = '+'
    elif operation in ["2", "-"]:
        operation = '-'
    elif operation in ["3", "x"]:
        operation = 'x'
    else:
        operation = '/'

    return operation

def display_result(n1, n2, operation, ans, lang = 'en'):
    '''displays the result of calculation'''
    print(MESSAGES[lang]['result'].format(a=n1,
                                            b=n2, op=operation, answer=ans))

def addition(num1, num2):
    '''performs addition of two numbers'''
    return num1 + num2

def subtraction(num1, num2):
    '''performs subtraction of two numbers'''
    return num1 - num2

def multiplication(num1, num2):
    '''multiplies two numbers'''
    return num1 * num2

def division(num1, num2):
    '''dividies two numbers'''
    try:
        return num1 / num2
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero")
        return e

def calculate(num1, num2, op):
    '''decides the calculation to be perfromed '''
    if op == '+':
        answer = addition(num1, num2)
    elif op == "-":
        answer = subtraction(num1, num2)
    elif op == "x":
        answer = multiplication(num1, num2)
    else:
        answer = division(num1, num2)

    if type(answer) == 'float':
        answer = round(answer, 2)
    return answer

def prompt_use_again(lang = 'en'):
    '''ask the user if he wants to use this calculator again'''
    while True:
        choice = input(MESSAGES[lang]['another_operation'])
        choice = choice.lower().strip()
        if choice not in CHOICE_OPTIONS:
            error_message()
        else:
            break

    return choice[0]

def main():
    language = prompt_language()
    welcome(language)
    while True:
        number1 = prompt_number1(language)
        number2 = prompt_number2(language)
        operation = prompt_operation(language)
        result = calculate(number1, number2, operation)
        display_result(number1, number2, operation, result, language)
        choice = prompt_use_again(language)
        if choice[0] == 'n':
            break
        os.system('cls || clear')
    goodbye(language)
if __name__ == "__main__":
    main()
