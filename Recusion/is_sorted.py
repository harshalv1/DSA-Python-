
def is_sorted(arr,size):
    if size==0 or size==1: #array with no or 1 element is sorted 
        return True
    elif arr[0]>arr[1]:
        return False
    
    else:
        return is_sorted(arr[1:],size-1) #every function call the list gets recursively smaller 
        #there is reduction in size of the array starting from the next element after the current element being compared. 
        # This allows the function to recursively check the remaining part of the array for sortedness.
    
arr=[2,3,4,5]
size=len(arr)

res=is_sorted(arr,size)
print(res)