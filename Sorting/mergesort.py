def merge_sort(arr):
    # Base case: if the array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort the left and right subarrays
    merge_sort(left)
    merge_sort(right)
    
    # Merge the sorted subarrays back into the original array
    i = j = k = 0
    
    # Compare elements from left and right subarrays and place them in the original array in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i=i+1
        else:
            arr[k] = right[j]
            j=j+ 1
        k=k+ 1
    
    # If there are any remaining elements in the left subarray, copy them to the original array
    while i < len(left):
        arr[k] = left[i]
        i=i+ 1
        k=k+ 1
    
    # If there are any remaining elements in the right subarray, copy them to the original array
    while j < len(right):
        arr[k] = right[j]
        j=j+ 1
        k=k+ 1
        
    # Return the sorted array
    return arr  

# Example usage
numbers = [8, 6, 4, 2, 1]
res = merge_sort(numbers)
print(res)
