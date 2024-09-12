def remove_duplicates(text):
    if not str(text):
        return text
    
    index = 1
    text_list = [text[0]]
    for i in text[1:]:
        if text_list[index - 1] != i:
            text_list.append(i)
            index += 1
        
    return ''.join(text_list)
        
# These examples should all print True
print(remove_duplicates('ddaaiillyy ddoouubbllee') == 'daily double')
print(remove_duplicates('4444abcabccba') == '4abcabcba')
print(remove_duplicates('ggggggggggggggg') == 'g')
print(remove_duplicates('abc') == 'abc')
print(remove_duplicates('a') == 'a')
print(remove_duplicates('') == '')

