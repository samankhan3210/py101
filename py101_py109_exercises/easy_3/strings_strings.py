def stringy(number):
    binary_str = ""
    for i in range(number):
        if i % 2 == 0:
            binary_str += '1'
        else:
            binary_str += '0'

    return binary_str

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True
