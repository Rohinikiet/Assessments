# Take user input for the string
sample_string = input("Enter a string: ")

char_frequency = {}

for char in sample_string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print(char_frequency)
