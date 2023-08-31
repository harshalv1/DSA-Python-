
arr_2d =[1,2,3,4,5,6]

def linearsearch(arr,key):

    for i in range(len(arr_2d)):
        if arr[i]==key:
            return i
        
    return -1
        
index=linearsearch(arr_2d,5)
print(f"our nber is at index {index}")