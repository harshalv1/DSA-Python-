#In the context of a rotated sorted array, the pivot element refers to the element at which the array's rotation occurs. It is the point where the array transitions from being sorted in ascending order to descending order.
#To understand this concept, let's consider an example array: [4, 5, 6, 7, 0, 1, 2]. This array is sorted in ascending order initially, but it has been rotated to the right, causing the elements to shift. 
#The pivot element in this case is 0 since it marks the point of rotation.

def get_pivot(arr):
    start=0
    end=len(arr)-1
    mid=start+(end-start)//2

    while start<end:

        if arr[0]<arr[mid]:
            start=mid+1
        
        else:
            end=mid

        mid=start+(end-start)//2
    
    return start

arr_2d=[7,9,1,2,3]
pivot_index=get_pivot(arr_2d)
print(f"The pivot is at {pivot_index}th position")