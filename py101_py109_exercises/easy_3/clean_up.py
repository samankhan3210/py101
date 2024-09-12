def is_ascii_letter(char):
    return char.isalpha() and char.isascii()

def clean_up(text):
    clean_text = ''

    for idx, char in enumerate(text):
        if is_ascii_letter(char):
            clean_text += char
        elif idx == 0 or clean_text[-1] != ' ':
            clean_text += ' '

    return clean_text

print(clean_up("---what's my +*& line?") == " what s my line ")
print(clean_up("Καλωσήρθες") == "Καλωσήρθες")   # True