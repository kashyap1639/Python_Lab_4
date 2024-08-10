def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]
    
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    
    return merge(left_list, right_list)

def merge(left_half, right_half):
    res = []
    left_index, right_index = 0, 0
    
    # Merge the two sorted arrays
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            res.append(left_half[left_index])
            left_index += 1
        else:
            res.append(right_half[right_index])
            right_index += 1
    
    # If there are remaining elements in left_half
    while left_index < len(left_half):
        res.append(left_half[left_index])
        left_index += 1
    
    # If there are remaining elements in right_half
    while right_index < len(right_half):
        res.append(right_half[right_index])
        right_index += 1
    
    return res

# Example usage
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(unsorted_list))
