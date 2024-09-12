def is_leap_year(year):
    if year < 1752:
        return year % 4 == 0
    else:
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def input_validation(year):
    try:
        return isinstance(int(year), int) and int(year) >= 1
    except ValueError:
        return False

def main():
    while True:
        input_year = input("Enter Year : ")
        if input_validation(input_year):
            break
        else:
            print("Invalid Input")

    if is_leap_year(int(input_year)):
        print(f'{input_year} is a leap year.')
    
    else:
        print(f'{input_year} is not a leap year.')
    
if __name__ == "__main__":
    main()