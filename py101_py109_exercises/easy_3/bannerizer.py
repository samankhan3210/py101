def get_border(len_of_msg):
    horizontal_rule = f'+-{"-" * (len_of_msg)}-+'
    empty_line = f'| {" " * (len_of_msg)} |'
    return horizontal_rule, empty_line

def print_in_box(message, width = 0):
    if width:

        len_trunc_msg = len(message[0:width-4])
        horizontal, empty = get_border(len_trunc_msg)
        print(horizontal)
        print(empty)

        while message:
            trunc_message = message[0:width-4]
            message = message[width-4:]
                
            print(f'| {trunc_message} |')

        print(empty)
        print(horizontal)

    else:
        horizontal, empty = get_border(len(message))
        print(horizontal)
        print(empty)
        print(f'| {message} |')
        print(empty)
        print(horizontal)

print_in_box('To boldly go where no one has gone before.', 10)