
def rotate_arr(arr,k):
    n=len(arr)
    temp=[0]*n #initializing temp array we want to have the same no of elements in temp array as our main array be and we want some element in the array therefore 0
    for i in range(n):
        temp[(i+k)%n]=arr[i] #populating the temp array in a cyclic manner 
    return temp

ns=[5,6,9,10,11,12,13]
k=3
rotated_arr=rotate_arr(ns,k)
print(rotated_arr)
    
            
