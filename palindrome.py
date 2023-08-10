def is_symmetrical(s):
    return s == s[::-1]

def is_palindrome(s):
    mid = len(s) // 2
    return s[:mid] == s[mid:][::-1]

input_string = input("Enter a string: ")

if is_symmetrical(input_string):
    print("The entered string is symmetrical")
else:
    print("The entered string is not symmetrical")

if is_palindrome(input_string):
    print("The entered string is palindrome")
else:
    print("The entered string is not palindrome")
