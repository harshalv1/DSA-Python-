
def Binarysearch(arr,s,e,k):

    if s>e:
        return False
    
    mid=s+(e-s)//2
    if arr[mid]==k:
        return True
    
    elif k>arr[mid]:
        return Binarysearch(arr,mid+1,e,k)

    else:
        return Binarysearch(arr,s,mid-1,k)
    

arr=[1,4,6,10,12,16]
s=0
e=len(arr)-1
k=12
Binarysearch(arr,s,e,k)

if Binarysearch(arr,s,e,k):
    print("Found")

else:
    print("Not found")