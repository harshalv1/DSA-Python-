def areBracketsMatching(expression):
    stack = []  # Initialize the stack inside the function
    for ch in expression: #iterate over the expression
        if ch == "{" or ch == "[" or ch == "(": #if we find opening bracket 
            stack.append(ch) #append that character of the expression in the stack 
        else:
            if len(stack) != 0: #we have to ensure that we haven't exhaused the stack 
                if (ch == "}" and stack[-1] == "{") or (ch == "]" and stack[-1] == "[") or (ch == ")" and stack[-1] == "("):
                    stack.pop() # if we find closing brackets which are corresponding to the opening brackets 
                    # we start to pop the elements
                else:
                    return False #only closing found therefore no match
            else:  
                return False #closing bracket is encountered, but there is no corresponding opening bracket in the stack
        
    if len(stack) == 0: #if the stack is exhaused that means we found a valid bracket /matching bracket 
        return True
    else:
        return False #stack is not exhausted that means we have not found a valid br

# Test cases
expression1 = "{[()]}"
expression2 = "{[(])}"
expression3 = "{[}"
expression4 = "}"

print(areBracketsMatching(expression1))  # True
print(areBracketsMatching(expression2))  # False
print(areBracketsMatching(expression3))  # False
print(areBracketsMatching(expression4))  # False
