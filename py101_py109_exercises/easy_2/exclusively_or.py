# def xor(a, b):
#     if (a and b) or ((not a) and (not b)):
#         return False
#     else:
#         return True
    
def xor(value1, value2):
    return bool((value1 and not value2) or (value2 and not value1))

print(xor(0, 5) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)