
def move_zeroes(arr):
    i=0 # represents the non zero value starting with index 0
    for j in range(len(arr)):
        if arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i=i+1
    return arr

ns=[0,1,0,3,12]
output=move_zeroes(ns)
print(output)
