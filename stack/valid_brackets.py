def is_valid(str):
    stack=[] 
    for i in range(len(str)):
        ch=str[i]
        
        if ch=="(" or ch=="{" or ch=="[": #if opening bracket stack push 
            stack.append(ch)
        
        else:
            #closing brackets check top and then pop  
            if len(stack)>0 :
                top=stack[-1]
                
                if (ch==")" and top=="(" ) or (ch=="}" and top=="{") or (ch=="]" and top=="["):
                    stack.pop()
                else:
                    return False
                
            else: #if only closing brackets are present and no corresponding open bracket is present 
                return False
    
    if len(stack)==0:
        return True
    else:
        return False
                


print(is_valid("{[]}"))  # Expected output: True (Valid)
print(is_valid(""))  # Expected output: True (Valid, an empty string is also considered valid)
print(is_valid("[[[[[[{}]]]]]]"))  # Expected output: True (Valid)
print(is_valid("({[})"))  # Expected output: False (Invalid)            
print(is_valid("()"))  # Expected output: True (Valid)
print(is_valid("()[]{}"))  # Expected output: True (Valid)
print(is_valid("(]"))  # Expected output: False (Invalid)
print(is_valid("([)]"))  # Expected output: False (Invalid)

