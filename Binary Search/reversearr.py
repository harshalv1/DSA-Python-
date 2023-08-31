def reversearr(arr):
    n=len(arr)
    for i in range(n//2):
        arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    return arr

ns=[5,4,3,2,1]

output=reversearr(ns)
print(f"The sorted array is {output}")

