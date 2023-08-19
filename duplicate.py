def remove_duplicates(input_array):
    unique_elements = []

    for element in input_array:
        if element not in unique_elements:
            unique_elements.append(element)

    return unique_elements
input_str = input("Enter a list of numbers separated by spaces: ")
input_array = list(map(int, input_str.split()))

result = remove_duplicates(input_array)

print("Original array:", " ".join(map(str, input_array)))
print("After removing duplicate elements from the said array:", " ".join(map(str, result)))
