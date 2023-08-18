def find_missing_number(arr):
    for num in range(10, 21):
        if num not in arr:
            return num

# Take user input for the array
input_str = input("Enter the array of numbers between 10 and 20, separated by spaces: ")
user_array = list(map(int, input_str.split()))

missing_number = find_missing_number(user_array)

print("Original array:", " ".join(map(str, user_array)))
print(f"Missing number in the said array (10-20): {missing_number}")
