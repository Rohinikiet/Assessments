
user_input = input("Enter a list of numbers separated by spaces: ")
user_list = [int(x) for x in user_input.split()]

non_zero_elements = []
zero_count = 0

for num in user_list:
    if num != 0:
        non_zero_elements.append(num)
    else:
        zero_count += 1

result = non_zero_elements + [0] * zero_count

print("Result:", result)
