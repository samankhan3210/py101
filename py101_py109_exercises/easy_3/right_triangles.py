def triangle(num):
    for i in range(1, num+1):
        space = ' ' * (num - i)
        stars = '*' * i
        print(f'{space}{stars}')

triangle(5)
print()
triangle(9)