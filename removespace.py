def remove_spaces(input_string):

    result_str = "".join(input_string.split())
    return result_str

input_str = input("enter the string:")

output_str = remove_spaces(input_str)
print(output_str)