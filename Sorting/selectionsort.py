def selection_sort(arr):

    for i in range(len(arr)):
        curr_min=i #assuming the smallest value in our array is at ith position in the array in first iteration it will be the first position
        for j in range(i+1,len(arr)):
            if arr[j]<arr[curr_min]: #if any element after the element at ith position is smaller than our min_value 
                curr_min=j #we update our minimum_index to the jth index 

        arr[curr_min], arr[i] = arr[i], arr[curr_min] # we swap the values

    return arr

ns=[6,2,8,4,10]
sorted_arr=selection_sort(ns)
print(f"The sorted array is : {sorted_arr}")
