def get_first_and_last_two_chars(input_string):

    if (len(input_string) < 2):
        return " "
    result = input_string[:2] + input_string[-2:]
    return result

input_string = input("enter string:")

result = get_first_and_last_two_chars(input_string)
print("Result:", result)