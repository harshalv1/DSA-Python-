
def knows(M,a,b,n):
    if M[a][b]==1:
        return True
    else:
        return False
        
def find_celeb(M,n):
    
    stack=[]
    
    for i in range(n):
        stack.append(i)
        
    while len(stack)!=1:
        a=stack.pop()
        b=stack.pop()
    
    if knows(M,a,b,n):
        stack.append(b)
        
    else:
        stack.append(a)
        
        
    ans=stack.pop() #found the celeb now lets verify
    
    zero_count=0
    
    for i in range(n):
        if M[ans][i]==0:
            zero_count=zero_count+1
    
    if zero_count!=n:
        return -1 
    
    one_count=0
    
    for i in range(n):
        if M[i][ans]==1:
            one_count=one_count+1
            
    if one_count!=n-1:
        return -1
        
    return ans
        
if __name__ == "__main__":
    M = [
        [0, 1, 1],
        [0, 0, 0],
        [1, 1, 0]
    ]
    n = 3
    result = find_celeb(M, n)

    if result != -1:
        print("The celebrity is person", result)
    else:
        print("There is no celebrity at the party.")
    
    