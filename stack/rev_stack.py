# Function to insert an element at the bottom of the stack
def insertAtBottom(stack, element):
    # If the stack is empty, simply append the element
    if len(stack) == 0:
        stack.append(element)
        return  # Return to stop further execution

    # Pop the top element from the stack
    top = stack[-1]
    stack.pop()

    # Recursively insert the element at the bottom of the stack
    insertAtBottom(stack, element)

    # Push the previously popped element back onto the stack
    stack.append(top)

# Function to reverse a stack
def rev_stack(stack):
    # Base case: If the stack is empty, return
    if len(stack) == 0:
        return

    # Pop an element from the stack
    num = stack.pop()

    # Recursively reverse the remaining stack
    rev_stack(stack)

    # Insert the popped element at the bottom of the reversed stack
    insertAtBottom(stack, num)


stack=[]
stack.append(3)
stack.append(2)
stack.append(1)
print(stack)
rev_stack(stack)
print(stack)