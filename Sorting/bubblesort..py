
def bub(arr):
    n=len(arr) #we go until len-1
    for i in range(n-1):
        for j in range(n-i-1): #we make n-i comparisions
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j] # swap the elements
    return arr
arr=[6,2,8,4,10]
res=bub(arr)
print(res) 
