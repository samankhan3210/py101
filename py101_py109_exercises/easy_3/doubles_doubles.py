# def twice(number):
#     str_num = str(number)
#     middle = len(str_num) // 2
#     is_double = True
#     for i in range(middle):
#         if str_num[i] != str_num[middle + i]:
#             is_double = False

#     if len(str_num) % 2 != 0 or is_double == False:
#         return number * 2
    
#     else:
#         return number
    
def is_double_number(number):
    string_number = str(number)
    center = len(string_number) // 2
    left_number = string_number[:center]
    right_number = string_number[center:]
    print(center, left_number, right_number)
    return left_number == right_number

def twice(number):
    if is_double_number(number):
        return number
    else:
        return number * 2
    
print(twice(1010101) == 202)   