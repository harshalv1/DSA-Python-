def is_valid(str):
    stack=[] 
    for i in range(len(str)):
        ch=str[i]
        
        if ch=="(" or ch=="{" or ch=="[":
            stack.append(ch)
        
        else:
            #closing brackets
            if len(stack)>0 :
                top=stack[-1]
                
                if (ch==")" and top=="(" ) or (ch=="}" and top=="{") or (ch=="]" and top=="["):
                    stack.pop()
                else:
                    return False
                
            else:
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

