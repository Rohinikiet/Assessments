def swap_first_last(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]

# Test cases
lists_to_swap = [
    [12, 35, 9, 56, 24],
    [24, 35, 9, 56, 12] ,
    [1, 2, 3] ,
    [3, 2, 1]
]

for lst in lists_to_swap:
    print("Original list:", lst)
    swap_first_last(lst)
    print("Swapped list:", lst)
    print()
