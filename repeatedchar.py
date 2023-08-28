def count_repeated_char(input_string):
    char_count = {}

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char,count in char_count.items():
        if count > 1:
            print(f"{char} {count}")

input_string = input("enter the string:")

count_repeated_char(input_string)