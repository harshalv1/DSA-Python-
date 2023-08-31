
def first(arr,s,e,key):
    if s>e: #when s>e i.e when we have exhausted all elements to search 
        return -1 # we return -1 i.e the element was not found 
    
    mid=s+(e-s)//2
    
    if arr[mid]==key: 
        if  mid==0 or arr[mid-1]!=key : #if we are on the first element 
             return mid                       
        else:
            return first(arr,s,mid-1,key)
    elif arr[mid]<key:
        return first(arr,mid+1,e,key) 
    else:
        return first(arr,s,mid-1,key) 
    

def last(arr,s,e,key):
    if s>e:
        return -1
    
    mid=s+(e-s)//2
    
    if arr[mid]==key:
        if mid==len(arr)-1 or arr[mid+1]!=key  :
            return mid
        else:
            return last(arr,mid+1,e,key)
    elif arr[mid]<key:
        return last(arr,mid+1,e,key) 
    else:
        return last(arr,s,mid-1,key) 
    
arr = [1, 2, 3, 3, 4, 4, 5, 5, 5]
key = 3
first_occ=first(arr,0,len(arr)-1,key)
last_occ=last(arr,0,len(arr)-1,key)
print(first_occ)
print(last_occ)
