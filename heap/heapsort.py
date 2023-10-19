

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



def heapsort(arr,n):
    size=n

    while size>1:
        arr[1],arr[size-1]=arr[size-1],arr[1]
        size-=1
        heapify(arr,size,1)
    


arr=[-1,50,60,55,45,70]

n=len(arr)

for i in range(n//2,0,-1):
    heapify(arr,n,i)

print(arr[1:])

heapsort(arr,n)
print(arr[1:])
    

#time complexity is o(nlogn) 