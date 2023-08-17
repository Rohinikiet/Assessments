from array import array

def count_occurrences(arr, target):
    return arr.count(target)

original_array = array('i', [5,8,9,4,5,3,5])

element_to_count = 5

occurrences = count_occurrences(original_array, element_to_count)

print("Original array:", original_array)
print(f"Number of occurrences of the number {element_to_count} in the said array:", occurrences)
