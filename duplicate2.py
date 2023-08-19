def remove_duplicates(input_array):
    # Initialize an empty list to store unique elements
    unique_elements = []

    # Iterate through the input array
    for element in input_array:
        # If the element is not in unique_elements, add it
        if element not in unique_elements:
            unique_elements.append(element)

    return unique_elements

# Sample input arrays
array1 = [1, 3, 5, 1, 3, 7, 9]

# Remove duplicates and print the results
result1 = remove_duplicates(array1)

print("Original array:", " ".join(map(str, array1)))
print("After removing duplicate elements from the said array:", " ".join(map(str, result1)))

