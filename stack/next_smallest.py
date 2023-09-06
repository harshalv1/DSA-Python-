

def next_smallest(arr,n):
    st=[-1]
    ans=[0]*n

    for i in range(len(arr)-1,-1,-1):
        curr=arr[i]
        while st[-1]>=curr:
            st.pop()
        ans[i]=st[-1]

        st.append(curr)

    return ans

arr=[2,1,4,3]
result=next_smallest(arr,4)
print(result)
