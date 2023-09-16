def part(arr, s, e):
    # Select the pivot element
    pivot = arr[s]
    
    count = 0
    # Count the number of elements smaller than the pivot
    for i in range(s + 1, e + 1):
        if arr[i] < pivot:
            count = count + 1
    
    pivot_index = s + count
    
    # Swap the pivot element to its correct position
    arr[s], arr[pivot_index] = arr[pivot_index], arr[s]
    
    i = s 
    j = e
    
    # Partition the remaining elements around the pivot
    while i < pivot_index and j > pivot_index:
        while arr[i] < pivot_index:
            i = i + 1
        
        while arr[j] > pivot_index:
            j = j - 1
        
        if i < pivot_index and j > pivot_index:
            arr[i], arr[j] = arr[j], arr[i]
    
    return pivot_index
            

def quick(arr, s, e):
    # Base case: return the array if s >= e
    if s >= e:
        return arr
        
    # Partition the array and get the partition index
    p = part(arr, s, e)
    
    # Recursively sort the subarrays
    quick(arr, s, p - 1)
    quick(arr, p + 1, e)
    
    return arr

# Test the quicksort algorithm
arr = [3, 1, 5, 2, 6]
sorted_arr = quick(arr, 0, len(arr) - 1)
print(sorted_arr)
