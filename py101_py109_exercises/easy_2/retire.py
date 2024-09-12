from datetime import datetime

current_age = int(input("What is your age? ")) 
retirement_age = int(input("At what age would you like to retire? "))
current_year = datetime.now().year
retirement_year = current_year + (retirement_age - current_age)
print(f"It's {current_year}. You will retire in {retirement_year}.\n"
      f"You have only {(retirement_age - current_age)} years of work to go!")
