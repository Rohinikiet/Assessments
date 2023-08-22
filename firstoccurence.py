from array import array

input_values = input("Enter array elements separated by spaces: ").split()
arr = array('i', map(int, input_values))

element_to_remove = int(input("Enter the element to remove: "))

if element_to_remove in arr:
    index_to_remove = arr.index(element_to_remove)
    arr.pop(index_to_remove)
    print("Original array:", arr)
else:
    print("Element not found in the array.")
