
def first_occur(arr,key):#first or shoud we say leftmost occurence

    start=0
    end=len(arr)-1
    mid=(start+end)//2

    while(start<=end):
        
        if arr[mid]==key:
            ans=mid 
            end=mid-1 #we shift the end to mid-1 hence discarding the right part 
        
        elif key>arr[mid]:
            start=mid+1

        else:
            end=mid-1
        
        mid=(start+end)//2

    return ans


def last_occur(arr,key): #or the rightmost occurence

    start=0
    end=len(arr)-1
    mid=(start+end)//2

    while(start<=end):
        
        if arr[mid]==key:
            ans=mid
            start=mid+1
        
        elif key>arr[mid]:
            start=mid+1

        else:
            end=mid-1
        
        mid=(start+end)//2

    return ans

even_arr=[1,2,3,3,3,4,5,6,6]
odd_arr=[6,6,7,8,9,10]

first_index=first_occur(even_arr,3)
last_index=last_occur(even_arr,3)
total_occurences=(last_index-first_index)+1
print(f"You would find the first occurence of 6 at {first_index}")
print(f"You would find the last occurence of 6 at {last_index}")
print(f"The total nber of occurences for the nber is {total_occurences}")