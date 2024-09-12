def multiple_of_3_and_5(number):
    summ = 0
    for i in range(1, number+1):
        if i % 3 ==0 or i % 5 == 0:
            summ += i
    
    return summ

def input_validation(x):
    try:
        return isinstance(int(x), int) and int(x) >= 1
    except ValueError:
        return False

def main():
    while True:
        num = input("Enter Number : ")
        if input_validation(num):
            break
        else:
            print("Invalid Input")

    print(multiple_of_3_and_5(int(num)))
    
if __name__ == "__main__":
    main()