def swap_first_and_last_chars(input_str):
    if len(input_str) < 2:
        return input_str  

    first_char = input_str[0]
    last_char = input_str[-1]
    middle_chars = input_str[1:-1]

    swapped_str = last_char + middle_chars + first_char
    return swapped_str

user_input = input("Enter a string: ")

result = swap_first_and_last_chars(user_input)
print("Result:", result)
