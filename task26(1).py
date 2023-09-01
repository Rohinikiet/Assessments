
input_number = input("Enter a number: ")

result = 1

for char in input_number:
    if char.isdigit():
        result *= int(char)

print("Multiplication of digits in the number:", result)
