def find_max_product_pair(arr):
    if len(arr) < 2:
        return None
    max1, max2, min1, min2 = float('-inf'), float('-inf'), float('inf'), float('inf')

    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    
    product1 = max1 * max2
    product2 = min1 * min2
    
    #  which pair has the higher product
    if product1 > product2:
        return (max2, max1)
    else:
        return (min1, min2)

original_array = [3,5,9,8,2,0,1]
result = find_max_product_pair(original_array)
if result:
    print(f"Maximum product pair is: {result}")
else:
    print("No pair found.")
