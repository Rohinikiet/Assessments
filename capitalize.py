def capitalize_first_and_last_letters(input_string):
    words = input_string.split()

    modified_words = []

    for word in words:
        if len(word) >= 2:
            # Capitalize the first letter and the last letter
            modified_word = word[0].upper() + word[1:-1] + word[-1].upper()
        else:
            # If the word has only one character, just capitalize it
            modified_word = word.upper()
        
        modified_words.append(modified_word)

    result_string = ' '.join(modified_words)

    return result_string

input_string = input("enter the string:")
result = capitalize_first_and_last_letters(input_string)
print(result)
