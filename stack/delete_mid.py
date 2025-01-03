class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def solve(stack, count, size):
    if count == size // 2:
        stack.pop()  # Remove the middle element from the stack
        return
    
    num = stack.pop()  # Pop the top element of the stack
    solve(stack, count + 1, size)  # Recur for the remaining elements
    stack.push(num)  # Push the element back onto the stack

def delete_mid(stack, size):
    count = 0
    solve(stack, count, size)  # Call the solve function to delete the middle element

stack = Stack()

# Push elements onto the stack
stack.push(5)
stack.push(1)
stack.push(7)
stack.push(2)
stack.push(6)

print("Original Stack:", stack.items)

# Delete the middle element
delete_mid(stack, stack.size())

print("Stack after deleting middle element:", stack.items)
#--------------------------------------------------------------------------------
#same solution but without creating a class stack
def solve(stack,count,size):
    if count==len(stack)//2:
        stack.pop()
        return
    
    num=stack.pop()
    solve(stack,count+1,size)
    stack.append(num)


def del_mid(stack,size):
    
    count=0
    solve(stack,count,size)

Stack=[]
Stack.append(1)
Stack.append(2)
Stack.append(3)
print(Stack)
del_mid(Stack,3)
print(Stack)
