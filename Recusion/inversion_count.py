def mergesort(arr):
    # Base case: if the array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr, 0  # Return the array and inversion count of 0
    
    mid = len(arr) // 2
    
    # Recursively sort the left and right subarrays and get their respective inversion counts
    left, count1 = mergesort(arr[:mid])
    right, count2 = mergesort(arr[mid:])
    
    i = j = k = 0
    count = count1 + count2  # Total inversion count
    
    # Compare elements from left and right subarrays and place them in the original array in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i=i + 1
        else:
            arr[k] = right[j]
            j=j+ 1
            count += len(left) - i  # Increment inversion count when elements from the right subarray are chosen before left
        k =k+ 1
        
    # If there are any remaining elements in the left subarray, copy them to the original array
    while i < len(left):
        arr[k] = left[i]
        i=i + 1
        k=k+ 1
    
    # If there are any remaining elements in the right subarray, copy them to the original array
    while j < len(right):
        arr[k] = right[j]
        j=j+ 1
        k=k+1
    
    # Return the sorted array and the inversion count
    return arr, count + count1 + count2

# Example usage
nums = [8, 6, 4, 2, 1]
sorted, track = mergesort(nums)
print(sorted)
print(track)
