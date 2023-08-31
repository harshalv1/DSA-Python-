def present(arr,target,i=0):
    if i>=len(arr):
        return False
    elif arr[i]==target:
        return True
    else:
        return present(arr,target,i+1)

arr=[1,2,3,4,5]
target=2

if present(arr,target):
    print("Found")
else:
    print("Not found")