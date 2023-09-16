
def insertion_sort(arr):
    for i in range(1,len(arr)): #assumption that the first element in the array is sorted
        key=arr[i] #created a key variable 
        j=i-1 
        while j>=0 and key<arr[j]: 
            arr[j+1]=arr[j] # shifting the position of the array to one index ahead 
            j=j-1 
        arr[j+1]=key # the key variable was replaced 
    return arr

ns=[6,1,8,5,3]

sorted_arr=insertion_sort(ns)
print(f"The sorted array is {sorted_arr}")
