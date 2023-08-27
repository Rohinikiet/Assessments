
input_str = input("Enter a comma-separated sequence of words: ")

words = input_str.split(',')

unique_words = set([word.strip() for word in words])

sorted_words = sorted(unique_words)

print(", ".join(sorted_words))
