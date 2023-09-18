def is_valid(str):

    brackets={"(":")","{":"}","[":"]"} #created a dict to store mappings 
    stack=[] # stack to append all open brackets
    
    for ch in str: # iterating through the str
        if ch in brackets: # if the ch has a key in the dict brackets then 
            stack.append(ch) # append the ch to the stack 
        elif len(stack)==0 or brackets[stack.pop()]!=ch: #str could contain only open brackets which would make the len of the str 0 after appending to the stack 
            return False # curr characters(closing brackets) corresponding opening bracket is on the top of the stack 
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

#T.C=o(N) coz of the for loop
#S.C=o(N)coz in the worst case the str could have only opening brackets