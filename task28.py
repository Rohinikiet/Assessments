
def find_longest_word_length(sentence):
    words = sentence.split()  
    max_length = 0  

    for word in words:
        word_length = len(word)
        if word_length > max_length:
            max_length = word_length

    return max_length

input_sentence = input("Enter a sentence: ")
result = find_longest_word_length(input_sentence)
print("largest length of the word:", result)
