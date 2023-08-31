# finding an element in a rotated sorted array through binary search approach
some_arr = [4, 5, 6, 7, 0, 1, 2]

def get_pivot(arr):
    start = 0
    end = len(arr) - 1
    mid = start + (end - start) // 2

    while start < end:
        if arr[0] <= arr[mid]:
            start = mid + 1
        else:
            end = mid
        mid = start + (end - start) // 2

    return start

def binary_search(arr, start, end, key):
    mid = start + (end - start) // 2

    while start <= end:
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
        mid = start + (end - start) // 2

    return -1

def searchforkey(arr,key):
    pivot=get_pivot(some_arr)

    if arr[pivot]<=key and key<=arr[len(arr)-1]: # if the key is in smaller line (visulaize graph of example)
        result=binary_search(some_arr,pivot,len(arr)-1,key) #applied binary search on smaller line 
    else: # if the key is in larger line 
        result=binary_search(some_arr,0,pivot-1,key) #applied binary search on that line 
 
    return result # returned the positioin of that no 

key=4
position=searchforkey(some_arr,key) # stored the result from searchforkey function in position variable 

if position==-1:
    print("Not found in array")
else:
    print(f"Found {key} at index {position}")