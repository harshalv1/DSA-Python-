
def heapify(arr,n,i):
    largest=i
    leftchild=2*i
    rightchild=2*i+1

    if leftchild<n and arr[largest]<arr[leftchild]:
        largest=leftchild
    
    if rightchild<n and arr[largest]<arr[rightchild]:
        largest=rightchild
        
    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]
        heapify(arr,n,largest)

arr=[-1,8, 12, 6, 4, 3, 1]

n=len(arr)

for i in range(n//2,0,-1):
    heapify(arr,n,i)

print(arr[1:])
    
