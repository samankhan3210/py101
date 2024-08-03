'''  a mortgage and a car payment calculator that determines the monthly payment 
    assuming that interest is compounded monthly. '''

import os
import json

with open('loan_calculator_messages.json', 'r', encoding='utf-8') as file:
    MESSAGES = json.load(file)

def validate_input_data(prompt):
    ''' validates the user input to make sure that it's a float value that is non-zero. '''
    while True:
        try:
            val = float(input(prompt))
            if val >= 0 and val != float('inf'):
                break

        except ValueError:
            print(MESSAGES["error_message"])

    return val

def loan_duration_validation(prompt1, prompt2):
    ''' validates the user input to make sure that the duration is valid '''
    while True:
        try:
            years = int(input(prompt1))
            months = int(input(prompt2))
            if years == 0 and months == 0:
                print("Both month(s) and year(s) cannot be 0!")
                print(MESSAGES['error_message'])
                continue
            if years >= 0 or months >= 0:
                break

        except ValueError:
            print(MESSAGES['error_message'])

    duration = (years * 12) + months
    print(duration)
    return duration

def calculate_monthly_amount(func_loan_amount, func_annual_percentage_rate, \
                             func_loan_duration_months):
    ''' uses the formula to calculate monthly payments based on the amount, duration, 
    and interest rate'''
    monthly_interest_rate = (func_annual_percentage_rate / 100 ) / 12
    denominator = (1 - (1 + monthly_interest_rate) ** (-func_loan_duration_months))
    monthly_payment = func_loan_amount * (monthly_interest_rate / denominator)
    monthly_payment = round(monthly_payment, 2)
    return monthly_payment

while True:
    print(MESSAGES["welcome"])
    loan_amount = validate_input_data(MESSAGES["loan_amount"])
    annual_percentage_rate = validate_input_data(MESSAGES["annual_percentage"])
    loan_duration_months = loan_duration_validation(
                                                    MESSAGES["duration_years"],
                                                    MESSAGES["duration_months"])
    monthly_payment_amount = calculate_monthly_amount(loan_amount, annual_percentage_rate,
                                                      loan_duration_months)
    print(f'Your monthly payment amount is : ${monthly_payment_amount}')
    choice_options = ['y', 'yes', 'yep', 'n', 'no', 'nope']
    while True:
        choice = input(MESSAGES["choice"])
        choice = choice.lower()
        os.system('cls')
        if choice not in choice_options:
            print("Incorrect Input, Try Again")
        else:
            break

    if choice[0] == 'n':
        break
