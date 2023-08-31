# Function to insert a number in the correct position in a sorted stack
def sorted_insert(stack, num):
    # Base case: If the stack is empty or the top element is smaller than the number
    if not stack or stack[-1] > num:
        stack.append(num)  # Insert the number at the top of the stack
        return
    
    n = stack.pop()  # Remove the top element from the stack
    
    # Recursive call: Insert the number in the correct position
    sorted_insert(stack, num)
    
    stack.append(n)  # Put back the removed element at the top

# Function to sort a stack using recursive sorting
def sort_stack(stack):
    # Base case: If the stack is empty
    if not stack:
        return
    
    num = stack.pop()  # Remove the top element from the stack
    
    # Recursive call: Sort the remaining elements in the stack
    sort_stack(stack)
    
    sorted_insert(stack, num)  # Insert the removed element in the sorted position

# Example usage
stack = [5, 8, 1, 2, 4]
sort_stack(stack)  # Sort the stack in descending order
print(stack)  # Output: [8, 5, 4, 2, 1]
