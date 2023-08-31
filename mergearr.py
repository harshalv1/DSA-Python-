
def merge_arrays(arr1,arr2):
    i=0
    j=0
    merged_array=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            merged_array.append(arr1[i])
            i=i+1
        else :
            merged_array.append(arr2[j])
            j=j+1
    merged_array=merged_array+(arr1[i:])
    merged_array=merged_array+(arr2[j:])
    return merged_array

arr1=[1,2,3,4]
arr2=[5,6,9,10,11,12]

merged_output=merge_arrays(arr1,arr2)
print(merged_output)