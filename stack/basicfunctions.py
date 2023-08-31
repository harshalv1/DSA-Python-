
stack=[]

stack.append(5)
stack.append(10)
stack.append(15)

removed_element=stack.pop()
top_element=stack[-1]
print(removed_element)
print(top_element)

if not stack:
    print("stack empty")

else:
    print("stack not empty")

print(len(stack))
