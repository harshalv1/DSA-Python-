def min_cost(str):
    
    if len(str)%2==1:
        return -1 
    else:
        stack=[]
        for ch in str:
            if ch=="{":
                stack.append(ch)
        else:
            while len(stack)!=0 and stack[-1]=="{":
                stack.pop()
            stack.append(ch)
            
        a=0 
        b=0
        while len(stack)!=0:
            if stack.pop()=="{":
                a=a+1
            else:
                b=b+1
        
        ans=(a+1)/2+(b+1)/2
        return ans

print(min_cost("{{}}"))  # Expected output: 1.0
print(min_cost("{{}{}"))  # Expected output: 2.0
print(min_cost("{{{{}}}}"))  # Expected output: 1.0
print(min_cost("{}{}{}{}"))  # Expected output: 2.0
print(min_cost("{{{{}}"))  # Expected output: -1 (Odd length)
print(min_cost("}}}}}}"))  # Expected output: -1 (Odd length)

                
            