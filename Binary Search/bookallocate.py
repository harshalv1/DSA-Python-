def is_possible(arr,n,m,mid):
    stud_count=1 
    page_sum=0

    for i in range(n):
        if page_sum+arr[i]<=mid:
            page_sum=page_sum+arr[i]
        else:
            stud_count=stud_count+1
            page_sum=arr[i]
            if stud_count>m:
                return False
            elif m>n:
                return False            
    return True


def allocate(arr,n,m):
    s=0
    sum_arr=0
    for i in range(n):
        sum_arr=sum_arr+arr[i]   
    e=sum_arr
    mid=s+(e-s)//2
    ans=-1

    while s<e:
        if is_possible(arr,n,m,mid):
            ans=mid
            e=mid-1

        else:
            s=mid+1
        mid=s+(e-s)//2
    return ans
    
ns=[10,20,30,40]  
n=4
m=2

output=allocate(ns,n,m)
print(f"The answer of the book allocation problem should be {output}")
