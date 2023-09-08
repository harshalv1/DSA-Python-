
def min_cost(str):
    stack=[]

    if len(str)%2!=0:
        return -1
    
    for i in range(len(str)):
            ch=str[i]
            
            if ch=="{":
                stack.append(ch)
            else:
                #ch is }
                if len(stack)>0 and stack[-1]=="{":
                    stack.pop()
                else:
                    stack.append(ch)

         
    a,b=0,0
    while len(stack)>0:
        if stack[-1]=="{":
            b=b+1
        else:
            a=a+1
        stack.pop()        
        
    ans = (a // 2) + (b // 2)


    return ans 
        

            