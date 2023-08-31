
def SqrtInt(n):
    start=0
    end=n
    mid=start+(end-start)//2

    while start<=end:
        if mid*mid==n:
            return mid
        elif mid*mid<=n:
            start=mid+1
        else:
            end=mid-1      
        mid=start+(end-start)//2
    return mid

n=144
sqrt=SqrtInt(n)
print(f"The sqrt is {sqrt}")

            
