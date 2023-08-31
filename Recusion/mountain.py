
#fetch mountain value 

def mountain(arr,s,e):
    
    if s>e:
        return -1
        
    mid=s+(e-s)//2
    
    if arr[mid-1]<arr[mid]>arr[mid+1]:
        return arr[mid]
    elif arr[mid]<arr[mid+1]:
        return mountain(arr,mid+1,e)       
    else:
        return mountain(arr,s,mid-1)

arr=[1,4,5,6,3,2]
peak=mountain(arr,0,len(arr)-1)
print(f"The peak value is {peak}")

      
    