'''  a mortgage and a car payment calculator that determines the monthly payment 
    assuming that interest is compounded monthly. '''

import os

def validate_input_data(prompt):
    ''' validates the user input to make sure that it's a float value that is non-zero '''
    while True:
        try:
            val = float(input(f'Please Enter the {prompt} : '))
            if val > 0:
                break
        except ValueError:
            print("Incorrect Input, Try Again!")

    return val

def loan_duration_validation(prompt):
    ''' takes the duration as a float and splits it into years and months, 
    it then converts that value into months, for example: 3.5 years is converted into 41 months. '''
    duration = validate_input_data(prompt)
    duration_str = f"{duration:.2f}"
    duration , months = duration_str.split('.')
    months = int(months)
    if months < 10:
        months = 0
    if months > 11 and months % 10 == 0 :
        months = int(months / 10)

    loan_duration = (int(duration) * 12) + months
    return loan_duration

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
    print("\n Welcome to the Loan Calculator \n")
    loan_amount = validate_input_data("Loan Amount")
    annual_percentage_rate = validate_input_data("Annual Percentage Rate (as '%' only, for " +
                                                "example 5 for 5% and 5.5 for 5.5%)")
    loan_duration_months = loan_duration_validation("Loan Duration (in years), " +
                                                    "for example 3 years 4 months as 3.4")
    monthly_payment_amount = calculate_monthly_amount(loan_amount, annual_percentage_rate, \
                                               loan_duration_months)
    print(f'Your monthly payment amount is : ${monthly_payment_amount}')
    choice = input("Do you want to perform another calculation (y/n)? ")
    choice = choice.lower()
    choice_options = ['y', 'yes', 'yep', 'n', 'no', 'nope']
    while choice not in choice_options:
        print("Incorrect Input, Try Again")
        choice = input("Do you want to perform another calculation (y/n)? ")
        choice = choice.lower()

    if choice[0] == 'n':
        break

    os.system('clear')
