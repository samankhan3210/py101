def greetings(name_lst, details_dict):
    full_name = ' '.join(name_lst)
    return f"Hello, {full_name}! Nice to have a {details_dict['title'] } {details_dict['occupation']} around."

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.

