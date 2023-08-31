
def binary_search(arr,key):
    start=0
    end=len(arr)-1
    mid=start+(end-start)//2 #we have used start+(end-start)//2 instead of s+e//2 coz of the range of integers which is 2^31-1 
    #if s and e have values 2^31-1 and if we try to add them we would get value greater the range so therefore we have a optimised way 

    while start<=end:

        if arr[mid]==key:
            return mid
        
        elif key<arr[mid]:
            end=mid-1

        else:
            start=mid+1

        mid=start+(end-start)//2
    return -1

even_arr=[2,3,4,5,7]
odd_arr=[3,5,10,11,13,15]

result=binary_search(odd_arr,11)
print(result)