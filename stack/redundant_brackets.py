def is_redundant(str):
    stack = []  # Initialize an empty stack to keep track of characters
    for i in range(len(str)):
        ch = str[i]

        if ch == "(" or ch == "+" or ch == "-" or ch == "*" or ch == "/":
            # If the character is an opening parenthesis or an operator, push it onto the stack
            stack.append(ch)
        else:
            if ch == ")":
                is_redundant = True  # Initialize a flag to check for redundant brackets

                top = None  # Initialize 'top' to an arbitrary value
                while top != "(" and len(stack) > 0:
                    top = stack.pop()  # Pop the top element from the stack
                    if top in "+-*/":
                        is_redundant = False  # If an operator is encountered, it's not redundant

                if is_redundant == True:
                    return True  # If is_redundant is still True, return True to indicate redundant brackets

    return False  # If no redundant brackets are found, return False

# Test cases
str1 = '(a+(b)/c)'  # Should return True (redundant brackets around '(b)')
str2 = '(a+c*b)+(c))'  # Should return True (redundant brackets around '(c))')
str3 = '(a*b+(c/d))'  # Should return False (no redundant brackets)
str4 = '((a/b))'  # Should return True (redundant brackets around '((a/b))')

print(is_redundant(str1))
print(is_redundant(str2))
print(is_redundant(str3))
print(is_redundant(str4))
