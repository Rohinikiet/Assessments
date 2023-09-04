def caesar_cipher(input_str):
    output_str = ""
    for char in input_str:
        if char.isalpha():
            shift = 5  
            if char.islower():
                shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            shifted_char = char
        
        output_str += shifted_char
    
    return output_str

input_str = input("enter the string:")
output_str = caesar_cipher(input_str)
print(output_str)  # Output: "btwi"
