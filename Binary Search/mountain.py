# imagine two lines one increasing and second decreasing the peak value is our desired output
def fetch_mountain(arr):
    start=0
    end=len(arr)-1


    while start<=end:
        mid=start+(end-start)//2 

        if arr[mid-1]<arr[mid]>arr[mid+1]: # we have to fetch the value whose left value is smaller and right is greater 
            return arr[mid]
        
        elif arr[mid-1]<arr[mid]: #as long as we find our value on the first line 
            start=mid+1 # we inrement the starte 
 
        else : #this is because the peak value could be on increasing line, mid value or decreasing line 
            end=mid #if our mid value is the peak then updating end=mid-1 would bring us on the increasing line 
               #which would not be desirable

    return -1 # if all else fails we return -1 i.e the value is not in the array

my_arr=[1,4,5,6,3,2]

mountain_value=fetch_mountain(my_arr)
print(f'The mountain value is {mountain_value}')
        
