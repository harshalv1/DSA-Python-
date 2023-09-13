from collections import deque

def modifyQueue(q, k):
    # Create a stack to temporarily store the first k elements
    stack = []
    
    # Convert the input list to a deque
    q = deque(q)

    # Move the first k elements from the front of the deque to the stack
    for i in range(k):
        value = q.popleft()
        stack.append(value)
    
    # Pop elements from the stack and enqueue them back into the deque, effectively reversing them
    while len(stack) != 0:
        val = stack.pop()
        q.append(val)

    # Dequeue the remaining (n-k) elements from the front and enqueue them back
    for _ in range(len(q) - k):
        num = q.popleft()
        q.append(num)

    return q
