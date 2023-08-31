def find_redundant_brackets(expression):
    st = []
    for ch in expression:
        if ch == "(" or ch == "+" or ch == "-" or ch == "*" or ch == "/":
            st.append(ch)
        elif ch == ")":
            is_redundant = True
            while len(st) > 0 and st[-1] != "(":
                if st[-s1] == "+" or st[-1] == "-" or st[-1] == "*" or st[-1] == "/":
                    is_redundant = False
                st.pop()
            if len(st) == 0:
                return True  # There's an unmatched closing bracket
            st.pop()
            if is_redundant:
                return True
    return False

expression = "((a+b)+(c-d))"
print(find_redundant_brackets(expression))  # Output: False

expression = "((a+b))"
print(find_redundant_brackets(expression))  # Output: True

expression = "(a+b)*(c-d)"
print(find_redundant_brackets(expression))  # Output: False

expression = "(a+b)"
print(find_redundant_brackets(expression))  # Output: False
