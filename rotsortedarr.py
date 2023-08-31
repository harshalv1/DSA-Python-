def rotsortedarr(arr): #checking if the given array is rotated sorted array 
    n=len(arr)
    count=0
    for i in range(1,n):
        if arr[i-1]>arr[i]: 
            count=count+1
    if arr[n-1]>arr[0]: #comparison of last and first element 
        count=count+1

    return count<=1 #if the count is 1 and 0 i.e all elements are equal return true and false for anything else

ns = [1, 2, 4, 6, 8, 12, 13]
value = rotsortedarr(ns)
print(value)
