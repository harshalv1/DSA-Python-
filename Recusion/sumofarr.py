
def sum(arr,i=0):
    if i>=len(arr):
        return 0
    
    else:
        return arr[i]+sum(arr,i+1)
        
arr=[1,2,3,4]
res=sum(arr)
print(res)
