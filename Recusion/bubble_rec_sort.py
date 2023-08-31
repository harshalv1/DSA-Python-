
def bubble_rec_sort(arr,n):
    
    if n<=1:
        return
    
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            bubble_rec_sort(arr,n-1)
    return arr
            
numbers=[1,7,4,9,10,5]
res=bubble_rec_sort(numbers,len(numbers))
print(res)