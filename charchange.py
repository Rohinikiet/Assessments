def replace_first_char_occurrences(input_str):
    if len(input_str) <= 1:
        return input_str

    first_char = input_str[0]
    modified_str = first_char  

    for char in input_str[1:]:
        if char == first_char:
            modified_str += '$'
        else:
            modified_str += char

    return modified_str

user_input = input("Enter a string: ")

result = replace_first_char_occurrences(user_input)
print("Result:", result)
