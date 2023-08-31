def merge(arr, s, mid, e):
    # Calculate the lengths of the subarrays
    len1 = mid - s + 1
    len2 = e - mid
    
    # Create temporary arrays to hold the subarrays
    arr1 = arr[s:mid+1]
    arr2 = arr[mid+1:e+1]
    
    # Initialize the indices for merging
    index1 = 0
    index2 = 0
    main_index = s
    
    # Merge the subarrays by comparing elements
    while index1 < len1 and index2 < len2:
        if arr1[index1] < arr2[index2]:
            arr[main_index] = arr1[index1]
            index1 += 1
        else:
            arr[main_index] = arr2[index2]
            index2 += 1
        main_index += 1    
    
    # Append remaining elements from arr1 (if any)
    while index1 < len1:
        arr[main_index] = arr1[index1]
        index1 += 1
        main_index += 1
        
    # Append remaining elements from arr2 (if any)
    while index2 < len2:
        arr[main_index] = arr2[index2]
        index2 += 1
        main_index += 1

def mergeSort(arr, s, e):
    # Base case: if s is greater than or equal to e, the array is already sorted
    if s >= e:
        return
    
    # Calculate the middle index
    mid = s + (e - s) // 2
    # Recursively sort the left and right halves of the array
    mergeSort(arr, s, mid)
    mergeSort(arr, mid+1, e)
    
    # Merge the sorted halves
    merge(arr, s, mid, e)

arr = [13, 11, 9, 7, 5, 3, 1]
mergeSort(arr, 0, len(arr) - 1)
print(arr)
